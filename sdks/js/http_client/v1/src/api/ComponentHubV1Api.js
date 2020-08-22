// Copyright 2018-2020 Polyaxon, Inc.
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//      http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

/**
 * Polyaxon SDKs and REST API specification.
 * Polyaxon SDKs and REST API specification.
 *
 * The version of the OpenAPI document: 1.1.8-rc0
 * Contact: contact@polyaxon.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */


import ApiClient from "../ApiClient";
import RuntimeError from '../model/RuntimeError';
import V1ComponentHub from '../model/V1ComponentHub';
import V1ListComponentHubsResponse from '../model/V1ListComponentHubsResponse';

/**
* ComponentHubV1 service.
* @module api/ComponentHubV1Api
* @version 1.1.8-rc0
*/
export default class ComponentHubV1Api {

    /**
    * Constructs a new ComponentHubV1Api. 
    * Polyaxon sdk
    * @alias module:api/ComponentHubV1Api
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the createComponentHub operation.
     * @callback module:api/ComponentHubV1Api~createComponentHubCallback
     * @param {String} error Error message, if any.
     * @param {module:model/V1ComponentHub} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Create hub component
     * @param {String} owner Owner of the namespace
     * @param {module:model/V1ComponentHub} body Component body
     * @param {module:api/ComponentHubV1Api~createComponentHubCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/V1ComponentHub}
     */
    createComponentHub(owner, body, callback) {
      let postBody = body;
      // verify the required parameter 'owner' is set
      if (owner === undefined || owner === null) {
        throw new Error("Missing the required parameter 'owner' when calling createComponentHub");
      }
      // verify the required parameter 'body' is set
      if (body === undefined || body === null) {
        throw new Error("Missing the required parameter 'body' when calling createComponentHub");
      }

      let pathParams = {
        'owner': owner
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['ApiKey'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = V1ComponentHub;
      return this.apiClient.callApi(
        '/api/v1/orgs/{owner}/components', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the deleteComponentHub operation.
     * @callback module:api/ComponentHubV1Api~deleteComponentHubCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Delete hub component
     * @param {String} owner Owner of the namespace
     * @param {String} uuid Uuid identifier of the entity
     * @param {module:api/ComponentHubV1Api~deleteComponentHubCallback} callback The callback function, accepting three arguments: error, data, response
     */
    deleteComponentHub(owner, uuid, callback) {
      let postBody = null;
      // verify the required parameter 'owner' is set
      if (owner === undefined || owner === null) {
        throw new Error("Missing the required parameter 'owner' when calling deleteComponentHub");
      }
      // verify the required parameter 'uuid' is set
      if (uuid === undefined || uuid === null) {
        throw new Error("Missing the required parameter 'uuid' when calling deleteComponentHub");
      }

      let pathParams = {
        'owner': owner,
        'uuid': uuid
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['ApiKey'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = null;
      return this.apiClient.callApi(
        '/api/v1/orgs/{owner}/components/{uuid}', 'DELETE',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getComponentHub operation.
     * @callback module:api/ComponentHubV1Api~getComponentHubCallback
     * @param {String} error Error message, if any.
     * @param {module:model/V1ComponentHub} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get hub component
     * @param {String} owner Owner of the namespace
     * @param {String} uuid Uuid identifier of the entity
     * @param {module:api/ComponentHubV1Api~getComponentHubCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/V1ComponentHub}
     */
    getComponentHub(owner, uuid, callback) {
      let postBody = null;
      // verify the required parameter 'owner' is set
      if (owner === undefined || owner === null) {
        throw new Error("Missing the required parameter 'owner' when calling getComponentHub");
      }
      // verify the required parameter 'uuid' is set
      if (uuid === undefined || uuid === null) {
        throw new Error("Missing the required parameter 'uuid' when calling getComponentHub");
      }

      let pathParams = {
        'owner': owner,
        'uuid': uuid
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['ApiKey'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = V1ComponentHub;
      return this.apiClient.callApi(
        '/api/v1/orgs/{owner}/components/{uuid}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the listComponentHubNames operation.
     * @callback module:api/ComponentHubV1Api~listComponentHubNamesCallback
     * @param {String} error Error message, if any.
     * @param {module:model/V1ListComponentHubsResponse} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * List hub component names
     * @param {String} owner Owner of the namespace
     * @param {Object} opts Optional parameters
     * @param {Number} opts.offset Pagination offset.
     * @param {Number} opts.limit Limit size.
     * @param {String} opts.sort Sort to order the search.
     * @param {String} opts.query Query filter the search search.
     * @param {module:api/ComponentHubV1Api~listComponentHubNamesCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/V1ListComponentHubsResponse}
     */
    listComponentHubNames(owner, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'owner' is set
      if (owner === undefined || owner === null) {
        throw new Error("Missing the required parameter 'owner' when calling listComponentHubNames");
      }

      let pathParams = {
        'owner': owner
      };
      let queryParams = {
        'offset': opts['offset'],
        'limit': opts['limit'],
        'sort': opts['sort'],
        'query': opts['query']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['ApiKey'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = V1ListComponentHubsResponse;
      return this.apiClient.callApi(
        '/api/v1/orgs/{owner}/components/names', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the listComponentHubs operation.
     * @callback module:api/ComponentHubV1Api~listComponentHubsCallback
     * @param {String} error Error message, if any.
     * @param {module:model/V1ListComponentHubsResponse} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * List hub components
     * @param {String} owner Owner of the namespace
     * @param {Object} opts Optional parameters
     * @param {Number} opts.offset Pagination offset.
     * @param {Number} opts.limit Limit size.
     * @param {String} opts.sort Sort to order the search.
     * @param {String} opts.query Query filter the search search.
     * @param {module:api/ComponentHubV1Api~listComponentHubsCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/V1ListComponentHubsResponse}
     */
    listComponentHubs(owner, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'owner' is set
      if (owner === undefined || owner === null) {
        throw new Error("Missing the required parameter 'owner' when calling listComponentHubs");
      }

      let pathParams = {
        'owner': owner
      };
      let queryParams = {
        'offset': opts['offset'],
        'limit': opts['limit'],
        'sort': opts['sort'],
        'query': opts['query']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['ApiKey'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = V1ListComponentHubsResponse;
      return this.apiClient.callApi(
        '/api/v1/orgs/{owner}/components', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the patchComponentHub operation.
     * @callback module:api/ComponentHubV1Api~patchComponentHubCallback
     * @param {String} error Error message, if any.
     * @param {module:model/V1ComponentHub} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Patch hub component
     * @param {String} owner Owner of the namespace
     * @param {String} component_uuid UUID
     * @param {module:model/V1ComponentHub} body Component body
     * @param {module:api/ComponentHubV1Api~patchComponentHubCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/V1ComponentHub}
     */
    patchComponentHub(owner, component_uuid, body, callback) {
      let postBody = body;
      // verify the required parameter 'owner' is set
      if (owner === undefined || owner === null) {
        throw new Error("Missing the required parameter 'owner' when calling patchComponentHub");
      }
      // verify the required parameter 'component_uuid' is set
      if (component_uuid === undefined || component_uuid === null) {
        throw new Error("Missing the required parameter 'component_uuid' when calling patchComponentHub");
      }
      // verify the required parameter 'body' is set
      if (body === undefined || body === null) {
        throw new Error("Missing the required parameter 'body' when calling patchComponentHub");
      }

      let pathParams = {
        'owner': owner,
        'component.uuid': component_uuid
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['ApiKey'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = V1ComponentHub;
      return this.apiClient.callApi(
        '/api/v1/orgs/{owner}/components/{component.uuid}', 'PATCH',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the updateComponentHub operation.
     * @callback module:api/ComponentHubV1Api~updateComponentHubCallback
     * @param {String} error Error message, if any.
     * @param {module:model/V1ComponentHub} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Update hub component
     * @param {String} owner Owner of the namespace
     * @param {String} component_uuid UUID
     * @param {module:model/V1ComponentHub} body Component body
     * @param {module:api/ComponentHubV1Api~updateComponentHubCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/V1ComponentHub}
     */
    updateComponentHub(owner, component_uuid, body, callback) {
      let postBody = body;
      // verify the required parameter 'owner' is set
      if (owner === undefined || owner === null) {
        throw new Error("Missing the required parameter 'owner' when calling updateComponentHub");
      }
      // verify the required parameter 'component_uuid' is set
      if (component_uuid === undefined || component_uuid === null) {
        throw new Error("Missing the required parameter 'component_uuid' when calling updateComponentHub");
      }
      // verify the required parameter 'body' is set
      if (body === undefined || body === null) {
        throw new Error("Missing the required parameter 'body' when calling updateComponentHub");
      }

      let pathParams = {
        'owner': owner,
        'component.uuid': component_uuid
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['ApiKey'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = V1ComponentHub;
      return this.apiClient.callApi(
        '/api/v1/orgs/{owner}/components/{component.uuid}', 'PUT',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
