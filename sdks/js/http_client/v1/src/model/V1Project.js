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
 * The version of the OpenAPI document: 1.0.79
 * Contact: contact@polyaxon.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import V1ProjectSettings from './V1ProjectSettings';

/**
 * The V1Project model module.
 * @module model/V1Project
 * @version 1.0.79
 */
class V1Project {
  /**
   * Constructs a new <code>V1Project</code>.
   * @alias module:model/V1Project
   */
  constructor() {

    V1Project.initialize(this);
  }

  /**
   * Initializes the fields of this object.
   * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
   * Only for internal use.
   */
  static initialize(obj) {
  }

  /**
   * Constructs a <code>V1Project</code> from a plain JavaScript object, optionally creating a new instance.
   * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
   * @param {Object} data The plain JavaScript object bearing properties of interest.
   * @param {module:model/V1Project} obj Optional instance to populate.
   * @return {module:model/V1Project} The populated <code>V1Project</code> instance.
   */
  static constructFromObject(data, obj) {
    if (data) {
      obj = obj || new V1Project();

      if (data.hasOwnProperty('uuid')) {
        obj['uuid'] = ApiClient.convertToType(data['uuid'], 'String');
      }
      if (data.hasOwnProperty('user')) {
        obj['user'] = ApiClient.convertToType(data['user'], 'String');
      }
      if (data.hasOwnProperty('user_email')) {
        obj['user_email'] = ApiClient.convertToType(data['user_email'], 'String');
      }
      if (data.hasOwnProperty('owner')) {
        obj['owner'] = ApiClient.convertToType(data['owner'], 'String');
      }
      if (data.hasOwnProperty('name')) {
        obj['name'] = ApiClient.convertToType(data['name'], 'String');
      }
      if (data.hasOwnProperty('description')) {
        obj['description'] = ApiClient.convertToType(data['description'], 'String');
      }
      if (data.hasOwnProperty('tags')) {
        obj['tags'] = ApiClient.convertToType(data['tags'], ['String']);
      }
      if (data.hasOwnProperty('created_at')) {
        obj['created_at'] = ApiClient.convertToType(data['created_at'], 'Date');
      }
      if (data.hasOwnProperty('updated_at')) {
        obj['updated_at'] = ApiClient.convertToType(data['updated_at'], 'Date');
      }
      if (data.hasOwnProperty('is_public')) {
        obj['is_public'] = ApiClient.convertToType(data['is_public'], 'Boolean');
      }
      if (data.hasOwnProperty('deleted')) {
        obj['deleted'] = ApiClient.convertToType(data['deleted'], 'Boolean');
      }
      if (data.hasOwnProperty('bookmarked')) {
        obj['bookmarked'] = ApiClient.convertToType(data['bookmarked'], 'Boolean');
      }
      if (data.hasOwnProperty('readme')) {
        obj['readme'] = ApiClient.convertToType(data['readme'], 'String');
      }
      if (data.hasOwnProperty('settings')) {
        obj['settings'] = V1ProjectSettings.constructFromObject(data['settings']);
      }
      if (data.hasOwnProperty('teams')) {
        obj['teams'] = ApiClient.convertToType(data['teams'], ['String']);
      }
    }
    return obj;
  }


}

/**
 * @member {String} uuid
 */
V1Project.prototype['uuid'] = undefined;

/**
 * @member {String} user
 */
V1Project.prototype['user'] = undefined;

/**
 * @member {String} user_email
 */
V1Project.prototype['user_email'] = undefined;

/**
 * @member {String} owner
 */
V1Project.prototype['owner'] = undefined;

/**
 * @member {String} name
 */
V1Project.prototype['name'] = undefined;

/**
 * @member {String} description
 */
V1Project.prototype['description'] = undefined;

/**
 * @member {Array.<String>} tags
 */
V1Project.prototype['tags'] = undefined;

/**
 * @member {Date} created_at
 */
V1Project.prototype['created_at'] = undefined;

/**
 * @member {Date} updated_at
 */
V1Project.prototype['updated_at'] = undefined;

/**
 * @member {Boolean} is_public
 */
V1Project.prototype['is_public'] = undefined;

/**
 * @member {Boolean} deleted
 */
V1Project.prototype['deleted'] = undefined;

/**
 * @member {Boolean} bookmarked
 */
V1Project.prototype['bookmarked'] = undefined;

/**
 * @member {String} readme
 */
V1Project.prototype['readme'] = undefined;

/**
 * @member {module:model/V1ProjectSettings} settings
 */
V1Project.prototype['settings'] = undefined;

/**
 * @member {Array.<String>} teams
 */
V1Project.prototype['teams'] = undefined;


export default V1Project;
