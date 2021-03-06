"""
Copyright 2013 Rackspace

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""
import unittest2

from cloudroast.cloudkeep.barbican.fixtures import SecretsFixture
from cafe.drivers.unittest.decorators import tags
from cloudcafe.cloudkeep.common.states import SecretsStates


class SecretsAPI(SecretsFixture):

    @tags(type='positive')
    def test_adding_full_secret(self):
        """ Covers proper creation of secret with an expiration attribute set
        - Reported in Barbican GitHub Issue #76
        """
        resp = self.behaviors.create_secret_from_config()

        self.assertEqual(resp.status_code, 201)
        self.assertGreater(len(resp.id), 0)

    @tags(type='positive')
    def test_adding_secret_wout_expiration(self):
        """Covers creating a secret without an expiration."""
        resp = self.behaviors.create_secret_from_config(use_expiration=False)

        self.assertEqual(resp.status_code, 201)
        self.assertGreater(len(resp.id), 0)

    @tags(type='positive')
    def test_get_secret_metadata(self):
        """Covers getting and checking a secret's metadata."""
        resp = self.behaviors.create_secret_from_config(use_expiration=False)
        self.assertEqual(resp.status_code, 201)

        sec_resp = self.client.get_secret(secret_id=resp.id)
        metadata = sec_resp.entity

        self.assertEqual(sec_resp.status_code, 200)
        self.assertEqual(metadata.status, SecretsStates.STATUS_ACTIVE)
        self.assertEqual(metadata.name, self.config.name)
        self.assertEqual(metadata.cypher_type, self.config.cypher_type)
        self.assertEqual(metadata.algorithm, self.config.algorithm)
        self.assertEqual(metadata.bit_length, self.config.bit_length)

    @tags(type='positive')
    def test_get_secret(self):
        """Covers getting a secret's encrypted data."""
        resp = self.behaviors.create_secret_from_config(use_expiration=False)
        self.assertEqual(resp.status_code, 201)

        sec_resp = self.client.get_secret(secret_id=resp.id,
                                          mime_type=self.config.mime_type)
        self.assertEqual(sec_resp.status_code, 200)
        self.assertIn(self.config.plain_text, sec_resp.content)

    @tags(type='positive')
    def test_updating_a_secret(self):
        """Covers giving a secret data."""
        # Create
        resp = self.behaviors.create_secret_from_config(use_expiration=False,
                                                        use_plain_text=False)
        self.assertEqual(resp.status_code, 201)

        # Update
        update_resp = self.client.add_secret_plain_text(
            secret_id=resp.id,
            mime_type=self.config.mime_type,
            plain_text='testing_update_secret')
        self.assertEqual(update_resp.status_code, 200)

        # Get/Check Updated
        sec_resp = self.client.get_secret(secret_id=resp.id,
                                          mime_type=self.config.mime_type)
        self.assertIn('testing_update_secret', sec_resp.content)

    @tags(type='positive')
    def test_deleting_a_secret(self):
        """Covers deleting a secret."""
        resp = self.behaviors.create_secret_from_config(use_expiration=False,
                                                        use_plain_text=False)
        self.assertEqual(resp.status_code, 201)

        del_resp = self.behaviors.delete_secret(resp.id)
        self.assertEqual(del_resp.status_code, 200)

    @tags(type='positive')
    def test_get_secrets(self):
        """Covers getting a list of secret."""
        # Make sure we have at least one secret to list
        self.behaviors.create_secret_from_config(use_expiration=False)
        get_resp = self.client.get_secrets()
        self.assertEqual(get_resp.status_code, 200)

        secrets = get_resp.entity.secrets
        self.assertGreater(len(secrets), 0)
