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


from cafe.drivers.unittest.decorators import tags
from cloudroast.images.v2.fixtures import ImagesV2Fixture


class PutImageMembersTest(ImagesV2Fixture):

    @tags(type='smoke')
    def test_update_image_member_status_from_pending_to_accepted(self):
        """ Change the status of an image member to accepted.

        1) Add a member to an image
        2) Get the image member
        3) Verify that the member status is 'pending'
        4) Update the status of an image member to 'accepted'
        5) Verify the response code is 200
        6) Verify that the member status has been updated to 'accepted'
        """

    @tags(type='positive')
    def test_update_image_member_status_from_pending_to_rejected(self):
        """ Change the status of an image member to rejected.

        1) Add a member to an image
        2) Get the image member
        3) Verify that the member status is 'pending'
        4) Update the status of an image member to 'rejected'
        5) Verify the response code is 200
        6) Verify that the member status has been updated to 'rejected'
        """

    @tags(type='positive')
    def test_update_image_member_status_from_accepted_to_pending(self):
        """ Change the status of an image member to pending.

        1) Get the image member with status 'accepted'
        2) Update the status of an image member to 'pending'
        3) Verify the response code is 200
        4) Verify that the member status has been updated to 'pending'
        """

    @tags(type='positive')
    def test_update_image_member_status_from_rejected_to_accepted(self):
        """ Change the status of an image member to accepted.

        1) Add a member to an image
        2) Get the image member
        3) Verify that the member status is 'pending'
        4) Update the status of an image member to 'rejected'
        5) Verify the response code is 200
        6) Verify that the member status has been updated to 'rejected'
        7) Update the status of an image member to 'accepted'.
        8) Verify that image member status is 'accepted'
        """

    @tags(type='positive')
    def test_update_image_member_status_from_accepted_to_rejected(self):
        """ Change the status of an image member to rejected.

        1) Add a member to an image
        2) Get the image member
        3) Verify that the member status is 'pending'
        4) Update the status of an image member to 'accepted'
        5) Verify the response code is 200
        6) Verify that the member status has been updated to 'accepted'
        7) Update the status of an image member to 'rejected'.
        8) Verify that image member status is 'rejected'
        """

    @tags(type='positive')
    def test_update_image_member_status_from_rejected_to_pending(self):
        """ Change the status of an image member to rejected.

        1) Get the image member with status 'accepted'
        2) Update the status of an image member to 'rejected'
        3) Verify the response code is 200
        4) Verify that the member status has been updated to 'rejected'
        7) Update the status of an image member to 'pending'.
        8) Verify that image member status is 'pending'
        """

    @tags(type='negative')
    def test_update_image_member_status_for_nonexistent_image(self):
        """Change the status of image member for non-existing image id

        1) Update status of an image member without using image id.
        2) Verify the response code is 404.
        """

    @tags(type='negative')
    def test_update_image_member_status_for_invalid_image_id(self):
        """Change the status of image member that doesn't exist

        1) Update status of an image member that doesn't exist.
        2) Verify the response code is 404.
        """
