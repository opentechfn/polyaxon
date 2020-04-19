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

(function(root, factory) {
  if (typeof define === 'function' && define.amd) {
    // AMD.
    define(['expect.js', process.cwd() + '/src/index'], factory);
  } else if (typeof module === 'object' && module.exports) {
    // CommonJS-like environments that support module.exports, like Node.
    factory(require('expect.js'), require(process.cwd() + '/src/index'));
  } else {
    // Browser globals (root is window)
    factory(root.expect, root.PolyaxonSdk);
  }
}(this, function(expect, PolyaxonSdk) {
  'use strict';

  var instance;

  beforeEach(function () {
    instance = new PolyaxonSdk.V1Parallel();
  });

  var getProperty = function (object, getter, property) {
    // Use getter method if present; otherwise, get the property directly.
    if (typeof object[getter] === 'function')
      return object[getter]();
    else
      return object[property];
  }

  var setProperty = function (object, setter, property, value) {
    // Use setter method if present; otherwise, set the property directly.
    if (typeof object[setter] === 'function')
      object[setter](value);
    else
      object[property] = value;
  }

  describe('V1Parallel', function () {
    it('should create an instance of V1Parallel', function () {
      // uncomment below and update the code to test V1Parallel
      //var instane = new PolyaxonSdk.V1Parallel();
      //expect(instance).to.be.a(PolyaxonSdk.V1Parallel);
    });

    it('should have the property random (base name: "random")', function () {
      // uncomment below and update the code to test the property random
      //var instane = new PolyaxonSdk.V1Parallel();
      //expect(instance).to.be();
    });

    it('should have the property grid (base name: "grid")', function () {
      // uncomment below and update the code to test the property grid
      //var instane = new PolyaxonSdk.V1Parallel();
      //expect(instance).to.be();
    });

    it('should have the property hyperband (base name: "hyperband")', function () {
      // uncomment below and update the code to test the property hyperband
      //var instane = new PolyaxonSdk.V1Parallel();
      //expect(instance).to.be();
    });

    it('should have the property bayes (base name: "bayes")', function () {
      // uncomment below and update the code to test the property bayes
      //var instane = new PolyaxonSdk.V1Parallel();
      //expect(instance).to.be();
    });

    it('should have the property hyperopt (base name: "hyperopt")', function () {
      // uncomment below and update the code to test the property hyperopt
      //var instane = new PolyaxonSdk.V1Parallel();
      //expect(instance).to.be();
    });

    it('should have the property iterative (base name: "iterative")', function () {
      // uncomment below and update the code to test the property iterative
      //var instane = new PolyaxonSdk.V1Parallel();
      //expect(instance).to.be();
    });

    it('should have the property mapping (base name: "mapping")', function () {
      // uncomment below and update the code to test the property mapping
      //var instane = new PolyaxonSdk.V1Parallel();
      //expect(instance).to.be();
    });

  });

}));