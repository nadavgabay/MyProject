# -*- coding: utf-8 -*-

###############################################################################
#
# VisitorsToday
# Retrieves today's visitors, actions, average actions, average time, and bounce rate.
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

class VisitorsToday(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the VisitorsToday Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(VisitorsToday, self).__init__(temboo_session, '/Library/Clicky/VisitorsToday')


    def new_input_set(self):
        return VisitorsTodayInputSet()

    def _make_result_set(self, result, path):
        return VisitorsTodayResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return VisitorsTodayChoreographyExecution(session, exec_id, path)

class VisitorsTodayInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the VisitorsToday
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_Output(self, value):
        """
        Set the value of the Output input for this Choreo. ((optional, string) What format you want the returned data to be in. Accepted values: xml, php, json, csv. Defaults to 'xml'.)
        """
        super(VisitorsTodayInputSet, self)._set_input('Output', value)
    def set_SiteID(self, value):
        """
        Set the value of the SiteID input for this Choreo. ((required, integer) Your request must include the site's ID that you want to access data from. Available from your site preferences page.)
        """
        super(VisitorsTodayInputSet, self)._set_input('SiteID', value)
    def set_SiteKey(self, value):
        """
        Set the value of the SiteKey input for this Choreo. ((required, string) The unique key assigned to you when you first register with Clicky. Available from your site preferences page.)
        """
        super(VisitorsTodayInputSet, self)._set_input('SiteKey', value)
    def set_Type(self, value):
        """
        Set the value of the Type input for this Choreo. ((optional, string) The type of data you want to retrieve. Defaults to "visitors,actions,actions-average,time-average,bounce-rate".)
        """
        super(VisitorsTodayInputSet, self)._set_input('Type', value)

class VisitorsTodayResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the VisitorsToday Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Clicky formatted as specified in the Output parameter. Default is XML.)
        """
        return self._output.get('Response', None)

class VisitorsTodayChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return VisitorsTodayResultSet(response, path)
