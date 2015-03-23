# -*- coding: utf-8 -*-

###############################################################################
#
# PutObject
# Uploads a file to your Amazon S3 storage bucket.
#
# Python versions 2.6, 2.7, 3.x
#
# Copyright 2014, Temboo Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
# either express or implied. See the License for the specific
# language governing permissions and limitations under the License.
#
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class PutObject(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the PutObject Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(PutObject, self).__init__(temboo_session, '/Library/Amazon/S3/PutObject')


    def new_input_set(self):
        return PutObjectInputSet()

    def _make_result_set(self, result, path):
        return PutObjectResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return PutObjectChoreographyExecution(session, exec_id, path)

class PutObjectInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the PutObject
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_FileContents(self, value):
        """
        Set the value of the FileContents input for this Choreo. ((required, string) The Base64-encoded file contents that you want to upload to an AmazonS3 bucket. This is required unless providing a URL to a hosted file to upload, using the UploadSourceURL input.)
        """
        super(PutObjectInputSet, self)._set_input('FileContents', value)
    def set_AWSAccessKeyId(self, value):
        """
        Set the value of the AWSAccessKeyId input for this Choreo. ((required, string) The Access Key ID provided by Amazon Web Services.)
        """
        super(PutObjectInputSet, self)._set_input('AWSAccessKeyId', value)
    def set_AWSSecretKeyId(self, value):
        """
        Set the value of the AWSSecretKeyId input for this Choreo. ((required, string) The Secret Key ID provided by Amazon Web Services.)
        """
        super(PutObjectInputSet, self)._set_input('AWSSecretKeyId', value)
    def set_BucketName(self, value):
        """
        Set the value of the BucketName input for this Choreo. ((required, string) The name of the bucket that will be the file destination.)
        """
        super(PutObjectInputSet, self)._set_input('BucketName', value)
    def set_CannedACL(self, value):
        """
        Set the value of the CannedACL input for this Choreo. ((optional, string) By default all objects are private (only owner has full access control). Valid values: private, public-read, public-read-write, authenticated-read, bucket-owner-read, bucket-owner-full-control.)
        """
        super(PutObjectInputSet, self)._set_input('CannedACL', value)
    def set_ContentType(self, value):
        """
        Set the value of the ContentType input for this Choreo. ((optional, string) Sets the content-type (text/html, image/jpeg, etc.). Default is application/octet-stream.)
        """
        super(PutObjectInputSet, self)._set_input('ContentType', value)
    def set_FileName(self, value):
        """
        Set the value of the FileName input for this Choreo. ((required, string) The name of the file to put in S3 Storage. Ex.: file.txt or folder/file.txt)
        """
        super(PutObjectInputSet, self)._set_input('FileName', value)
    def set_SSECAlgorithm(self, value):
        """
        Set the value of the SSECAlgorithm input for this Choreo. ((optional, string) Specifies the server-side encryption with customer-provided encryption keys (SSE-C) algorithm to use when Amazon S3 creates the target object. Valid value: AES256.)
        """
        super(PutObjectInputSet, self)._set_input('SSECAlgorithm', value)
    def set_SSECKey(self, value):
        """
        Set the value of the SSECKey input for this Choreo. ((optional, string) The customer-provided AES-256 256-bit (32-byte) encryption key for Amazon S3 to use to encrypt or decrypt your data.)
        """
        super(PutObjectInputSet, self)._set_input('SSECKey', value)
    def set_ServerSideEncryption(self, value):
        """
        Set the value of the ServerSideEncryption input for this Choreo. ((optional, string) Specifies the server-side encryption algorithm to use when Amazon S3 creates the target object. Valid value: AES256.)
        """
        super(PutObjectInputSet, self)._set_input('ServerSideEncryption', value)
    def set_StorageClass(self, value):
        """
        Set the value of the StorageClass input for this Choreo. ((optional, string) Enables RRS customers to store their noncritical, reproducible data at lower levels of redundancy than Amazon S3's standard storage. Valid Values: STANDARD (default), REDUCED_REDUNDANCY.)
        """
        super(PutObjectInputSet, self)._set_input('StorageClass', value)
    def set_UploadSourcePassword(self, value):
        """
        Set the value of the UploadSourcePassword input for this Choreo. ((optional, string) The password to use when Basic Authentiation is required to access a file located at the URL specified in the UploadSourceURL input.)
        """
        super(PutObjectInputSet, self)._set_input('UploadSourcePassword', value)
    def set_UploadSourceURL(self, value):
        """
        Set the value of the UploadSourceURL input for this Choreo. ((optional, string) A URL to a hosted file that should be uploaded. This is required unless providing a Base64 encoded file for the FileContents input.)
        """
        super(PutObjectInputSet, self)._set_input('UploadSourceURL', value)
    def set_UploadSourceUsername(self, value):
        """
        Set the value of the UploadSourceUsername input for this Choreo. ((optional, string) The username to use when Basic Authentiation is required to access a file located at the URL specified in the UploadSourceURL input.)
        """
        super(PutObjectInputSet, self)._set_input('UploadSourceUsername', value)
    def set_WebsiteRedirectLocation(self, value):
        """
        Set the value of the WebsiteRedirectLocation input for this Choreo. ((optional, string) If the bucket is configured as a website, redirects requests for this object to another object in the same bucket or to an external URL. Ex: /anotherPage.html, http://www.page.com. Max length: 2 K.)
        """
        super(PutObjectInputSet, self)._set_input('WebsiteRedirectLocation', value)


class PutObjectResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the PutObject Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Amazon. Note that no content is returned for successful uploads.)
        """
        return self._output.get('Response', None)

class PutObjectChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return PutObjectResultSet(response, path)
