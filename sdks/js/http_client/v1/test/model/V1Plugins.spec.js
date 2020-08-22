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

(function(root, factory) {
  if (typeof define === 'function' && define.amd) {
    // AMD.
    define(['expect.js', process.cwd()+'/src/index'], factory);
  } else if (typeof module === 'object' && module.exports) {
    // CommonJS-like environments that support module.exports, like Node.
    factory(require('expect.js'), require(process.cwd()+'/src/index'));
  } else {
    // Browser globals (root is window)
    factory(root.expect, root.PolyaxonSdk);
  }
}(this, function(expect, PolyaxonSdk) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new PolyaxonSdk.V1Plugins();
  });

  var getProperty = function(object, getter, property) {
    // Use getter method if present; otherwise, get the property directly.
    if (typeof object[getter] === 'function')
      return object[getter]();
    else
      return object[property];
  }

  var setProperty = function(object, setter, property, value) {
    // Use setter method if present; otherwise, set the property directly.
    if (typeof object[setter] === 'function')
      object[setter](value);
    else
      object[property] = value;
  }

  describe('V1Plugins', function() {
    it('should create an instance of V1Plugins', function() {
      // uncomment below and update the code to test V1Plugins
      //var instane = new PolyaxonSdk.V1Plugins();
      //expect(instance).to.be.a(PolyaxonSdk.V1Plugins);
    });

    it('should have the property auth (base name: "auth")', function() {
      // uncomment below and update the code to test the property auth
      //var instane = new PolyaxonSdk.V1Plugins();
      //expect(instance).to.be();
    });

    it('should have the property docker (base name: "docker")', function() {
      // uncomment below and update the code to test the property docker
      //var instane = new PolyaxonSdk.V1Plugins();
      //expect(instance).to.be();
    });

    it('should have the property shm (base name: "shm")', function() {
      // uncomment below and update the code to test the property shm
      //var instane = new PolyaxonSdk.V1Plugins();
      //expect(instance).to.be();
    });

    it('should have the property collect_artifacts (base name: "collect_artifacts")', function() {
      // uncomment below and update the code to test the property collect_artifacts
      //var instane = new PolyaxonSdk.V1Plugins();
      //expect(instance).to.be();
    });

    it('should have the property collect_logs (base name: "collect_logs")', function() {
      // uncomment below and update the code to test the property collect_logs
      //var instane = new PolyaxonSdk.V1Plugins();
      //expect(instance).to.be();
    });

    it('should have the property collect_resources (base name: "collect_resources")', function() {
      // uncomment below and update the code to test the property collect_resources
      //var instane = new PolyaxonSdk.V1Plugins();
      //expect(instance).to.be();
    });

    it('should have the property sync_statuses (base name: "sync_statuses")', function() {
      // uncomment below and update the code to test the property sync_statuses
      //var instane = new PolyaxonSdk.V1Plugins();
      //expect(instance).to.be();
    });

    it('should have the property auto_resume (base name: "auto_resume")', function() {
      // uncomment below and update the code to test the property auto_resume
      //var instane = new PolyaxonSdk.V1Plugins();
      //expect(instance).to.be();
    });

    it('should have the property log_level (base name: "log_level")', function() {
      // uncomment below and update the code to test the property log_level
      //var instane = new PolyaxonSdk.V1Plugins();
      //expect(instance).to.be();
    });

    it('should have the property notifications (base name: "notifications")', function() {
      // uncomment below and update the code to test the property notifications
      //var instane = new PolyaxonSdk.V1Plugins();
      //expect(instance).to.be();
    });

  });

}));
