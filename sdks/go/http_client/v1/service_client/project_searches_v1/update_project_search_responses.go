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

// Code generated by go-swagger; DO NOT EDIT.

package project_searches_v1

// This file was generated by the swagger tool.
// Editing this file might prove futile when you re-run the swagger generate command

import (
	"fmt"
	"io"

	"github.com/go-openapi/runtime"
	"github.com/go-openapi/strfmt"

	"github.com/polyaxon/polyaxon/sdks/go/http_client/v1/service_model"
)

// UpdateProjectSearchReader is a Reader for the UpdateProjectSearch structure.
type UpdateProjectSearchReader struct {
	formats strfmt.Registry
}

// ReadResponse reads a server response into the received o.
func (o *UpdateProjectSearchReader) ReadResponse(response runtime.ClientResponse, consumer runtime.Consumer) (interface{}, error) {
	switch response.Code() {
	case 200:
		result := NewUpdateProjectSearchOK()
		if err := result.readResponse(response, consumer, o.formats); err != nil {
			return nil, err
		}
		return result, nil
	case 204:
		result := NewUpdateProjectSearchNoContent()
		if err := result.readResponse(response, consumer, o.formats); err != nil {
			return nil, err
		}
		return result, nil
	case 403:
		result := NewUpdateProjectSearchForbidden()
		if err := result.readResponse(response, consumer, o.formats); err != nil {
			return nil, err
		}
		return nil, result
	case 404:
		result := NewUpdateProjectSearchNotFound()
		if err := result.readResponse(response, consumer, o.formats); err != nil {
			return nil, err
		}
		return nil, result
	default:
		result := NewUpdateProjectSearchDefault(response.Code())
		if err := result.readResponse(response, consumer, o.formats); err != nil {
			return nil, err
		}
		if response.Code()/100 == 2 {
			return result, nil
		}
		return nil, result
	}
}

// NewUpdateProjectSearchOK creates a UpdateProjectSearchOK with default headers values
func NewUpdateProjectSearchOK() *UpdateProjectSearchOK {
	return &UpdateProjectSearchOK{}
}

/*UpdateProjectSearchOK handles this case with default header values.

A successful response.
*/
type UpdateProjectSearchOK struct {
	Payload *service_model.V1Search
}

func (o *UpdateProjectSearchOK) Error() string {
	return fmt.Sprintf("[PUT /api/v1/{owner}/{project}/searches/{search.uuid}][%d] updateProjectSearchOK  %+v", 200, o.Payload)
}

func (o *UpdateProjectSearchOK) GetPayload() *service_model.V1Search {
	return o.Payload
}

func (o *UpdateProjectSearchOK) readResponse(response runtime.ClientResponse, consumer runtime.Consumer, formats strfmt.Registry) error {

	o.Payload = new(service_model.V1Search)

	// response payload
	if err := consumer.Consume(response.Body(), o.Payload); err != nil && err != io.EOF {
		return err
	}

	return nil
}

// NewUpdateProjectSearchNoContent creates a UpdateProjectSearchNoContent with default headers values
func NewUpdateProjectSearchNoContent() *UpdateProjectSearchNoContent {
	return &UpdateProjectSearchNoContent{}
}

/*UpdateProjectSearchNoContent handles this case with default header values.

No content.
*/
type UpdateProjectSearchNoContent struct {
	Payload interface{}
}

func (o *UpdateProjectSearchNoContent) Error() string {
	return fmt.Sprintf("[PUT /api/v1/{owner}/{project}/searches/{search.uuid}][%d] updateProjectSearchNoContent  %+v", 204, o.Payload)
}

func (o *UpdateProjectSearchNoContent) GetPayload() interface{} {
	return o.Payload
}

func (o *UpdateProjectSearchNoContent) readResponse(response runtime.ClientResponse, consumer runtime.Consumer, formats strfmt.Registry) error {

	// response payload
	if err := consumer.Consume(response.Body(), &o.Payload); err != nil && err != io.EOF {
		return err
	}

	return nil
}

// NewUpdateProjectSearchForbidden creates a UpdateProjectSearchForbidden with default headers values
func NewUpdateProjectSearchForbidden() *UpdateProjectSearchForbidden {
	return &UpdateProjectSearchForbidden{}
}

/*UpdateProjectSearchForbidden handles this case with default header values.

You don't have permission to access the resource.
*/
type UpdateProjectSearchForbidden struct {
	Payload interface{}
}

func (o *UpdateProjectSearchForbidden) Error() string {
	return fmt.Sprintf("[PUT /api/v1/{owner}/{project}/searches/{search.uuid}][%d] updateProjectSearchForbidden  %+v", 403, o.Payload)
}

func (o *UpdateProjectSearchForbidden) GetPayload() interface{} {
	return o.Payload
}

func (o *UpdateProjectSearchForbidden) readResponse(response runtime.ClientResponse, consumer runtime.Consumer, formats strfmt.Registry) error {

	// response payload
	if err := consumer.Consume(response.Body(), &o.Payload); err != nil && err != io.EOF {
		return err
	}

	return nil
}

// NewUpdateProjectSearchNotFound creates a UpdateProjectSearchNotFound with default headers values
func NewUpdateProjectSearchNotFound() *UpdateProjectSearchNotFound {
	return &UpdateProjectSearchNotFound{}
}

/*UpdateProjectSearchNotFound handles this case with default header values.

Resource does not exist.
*/
type UpdateProjectSearchNotFound struct {
	Payload interface{}
}

func (o *UpdateProjectSearchNotFound) Error() string {
	return fmt.Sprintf("[PUT /api/v1/{owner}/{project}/searches/{search.uuid}][%d] updateProjectSearchNotFound  %+v", 404, o.Payload)
}

func (o *UpdateProjectSearchNotFound) GetPayload() interface{} {
	return o.Payload
}

func (o *UpdateProjectSearchNotFound) readResponse(response runtime.ClientResponse, consumer runtime.Consumer, formats strfmt.Registry) error {

	// response payload
	if err := consumer.Consume(response.Body(), &o.Payload); err != nil && err != io.EOF {
		return err
	}

	return nil
}

// NewUpdateProjectSearchDefault creates a UpdateProjectSearchDefault with default headers values
func NewUpdateProjectSearchDefault(code int) *UpdateProjectSearchDefault {
	return &UpdateProjectSearchDefault{
		_statusCode: code,
	}
}

/*UpdateProjectSearchDefault handles this case with default header values.

An unexpected error response.
*/
type UpdateProjectSearchDefault struct {
	_statusCode int

	Payload *service_model.RuntimeError
}

// Code gets the status code for the update project search default response
func (o *UpdateProjectSearchDefault) Code() int {
	return o._statusCode
}

func (o *UpdateProjectSearchDefault) Error() string {
	return fmt.Sprintf("[PUT /api/v1/{owner}/{project}/searches/{search.uuid}][%d] UpdateProjectSearch default  %+v", o._statusCode, o.Payload)
}

func (o *UpdateProjectSearchDefault) GetPayload() *service_model.RuntimeError {
	return o.Payload
}

func (o *UpdateProjectSearchDefault) readResponse(response runtime.ClientResponse, consumer runtime.Consumer, formats strfmt.Registry) error {

	o.Payload = new(service_model.RuntimeError)

	// response payload
	if err := consumer.Consume(response.Body(), o.Payload); err != nil && err != io.EOF {
		return err
	}

	return nil
}
