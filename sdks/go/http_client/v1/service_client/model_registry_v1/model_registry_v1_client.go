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

package model_registry_v1

// This file was generated by the swagger tool.
// Editing this file might prove futile when you re-run the swagger generate command

import (
	"github.com/go-openapi/runtime"
	"github.com/go-openapi/strfmt"
)

// New creates a new model registry v1 API client.
func New(transport runtime.ClientTransport, formats strfmt.Registry) ClientService {
	return &Client{transport: transport, formats: formats}
}

/*
Client for model registry v1 API
*/
type Client struct {
	transport runtime.ClientTransport
	formats   strfmt.Registry
}

// ClientService is the interface for Client methods
type ClientService interface {
	CreateModelRegistry(params *CreateModelRegistryParams, authInfo runtime.ClientAuthInfoWriter) (*CreateModelRegistryOK, *CreateModelRegistryNoContent, error)

	DeleteModelRegistry(params *DeleteModelRegistryParams, authInfo runtime.ClientAuthInfoWriter) (*DeleteModelRegistryOK, *DeleteModelRegistryNoContent, error)

	GetModelRegistry(params *GetModelRegistryParams, authInfo runtime.ClientAuthInfoWriter) (*GetModelRegistryOK, *GetModelRegistryNoContent, error)

	ListModelRegistry(params *ListModelRegistryParams, authInfo runtime.ClientAuthInfoWriter) (*ListModelRegistryOK, *ListModelRegistryNoContent, error)

	ListModelRegistryNames(params *ListModelRegistryNamesParams, authInfo runtime.ClientAuthInfoWriter) (*ListModelRegistryNamesOK, *ListModelRegistryNamesNoContent, error)

	PatchModelRegistry(params *PatchModelRegistryParams, authInfo runtime.ClientAuthInfoWriter) (*PatchModelRegistryOK, *PatchModelRegistryNoContent, error)

	UpdateModelRegistry(params *UpdateModelRegistryParams, authInfo runtime.ClientAuthInfoWriter) (*UpdateModelRegistryOK, *UpdateModelRegistryNoContent, error)

	SetTransport(transport runtime.ClientTransport)
}

/*
  CreateModelRegistry creates hub model
*/
func (a *Client) CreateModelRegistry(params *CreateModelRegistryParams, authInfo runtime.ClientAuthInfoWriter) (*CreateModelRegistryOK, *CreateModelRegistryNoContent, error) {
	// TODO: Validate the params before sending
	if params == nil {
		params = NewCreateModelRegistryParams()
	}

	result, err := a.transport.Submit(&runtime.ClientOperation{
		ID:                 "CreateModelRegistry",
		Method:             "POST",
		PathPattern:        "/api/v1/orgs/{owner}/models",
		ProducesMediaTypes: []string{"application/json"},
		ConsumesMediaTypes: []string{"application/json"},
		Schemes:            []string{"http", "https"},
		Params:             params,
		Reader:             &CreateModelRegistryReader{formats: a.formats},
		AuthInfo:           authInfo,
		Context:            params.Context,
		Client:             params.HTTPClient,
	})
	if err != nil {
		return nil, nil, err
	}
	switch value := result.(type) {
	case *CreateModelRegistryOK:
		return value, nil, nil
	case *CreateModelRegistryNoContent:
		return nil, value, nil
	}
	// unexpected success response
	unexpectedSuccess := result.(*CreateModelRegistryDefault)
	return nil, nil, runtime.NewAPIError("unexpected success response: content available as default response in error", unexpectedSuccess, unexpectedSuccess.Code())
}

/*
  DeleteModelRegistry deletes hub model
*/
func (a *Client) DeleteModelRegistry(params *DeleteModelRegistryParams, authInfo runtime.ClientAuthInfoWriter) (*DeleteModelRegistryOK, *DeleteModelRegistryNoContent, error) {
	// TODO: Validate the params before sending
	if params == nil {
		params = NewDeleteModelRegistryParams()
	}

	result, err := a.transport.Submit(&runtime.ClientOperation{
		ID:                 "DeleteModelRegistry",
		Method:             "DELETE",
		PathPattern:        "/api/v1/orgs/{owner}/models/{uuid}",
		ProducesMediaTypes: []string{"application/json"},
		ConsumesMediaTypes: []string{"application/json"},
		Schemes:            []string{"http", "https"},
		Params:             params,
		Reader:             &DeleteModelRegistryReader{formats: a.formats},
		AuthInfo:           authInfo,
		Context:            params.Context,
		Client:             params.HTTPClient,
	})
	if err != nil {
		return nil, nil, err
	}
	switch value := result.(type) {
	case *DeleteModelRegistryOK:
		return value, nil, nil
	case *DeleteModelRegistryNoContent:
		return nil, value, nil
	}
	// unexpected success response
	unexpectedSuccess := result.(*DeleteModelRegistryDefault)
	return nil, nil, runtime.NewAPIError("unexpected success response: content available as default response in error", unexpectedSuccess, unexpectedSuccess.Code())
}

/*
  GetModelRegistry gets hub model
*/
func (a *Client) GetModelRegistry(params *GetModelRegistryParams, authInfo runtime.ClientAuthInfoWriter) (*GetModelRegistryOK, *GetModelRegistryNoContent, error) {
	// TODO: Validate the params before sending
	if params == nil {
		params = NewGetModelRegistryParams()
	}

	result, err := a.transport.Submit(&runtime.ClientOperation{
		ID:                 "GetModelRegistry",
		Method:             "GET",
		PathPattern:        "/api/v1/orgs/{owner}/models/{uuid}",
		ProducesMediaTypes: []string{"application/json"},
		ConsumesMediaTypes: []string{"application/json"},
		Schemes:            []string{"http", "https"},
		Params:             params,
		Reader:             &GetModelRegistryReader{formats: a.formats},
		AuthInfo:           authInfo,
		Context:            params.Context,
		Client:             params.HTTPClient,
	})
	if err != nil {
		return nil, nil, err
	}
	switch value := result.(type) {
	case *GetModelRegistryOK:
		return value, nil, nil
	case *GetModelRegistryNoContent:
		return nil, value, nil
	}
	// unexpected success response
	unexpectedSuccess := result.(*GetModelRegistryDefault)
	return nil, nil, runtime.NewAPIError("unexpected success response: content available as default response in error", unexpectedSuccess, unexpectedSuccess.Code())
}

/*
  ListModelRegistry lists hub models
*/
func (a *Client) ListModelRegistry(params *ListModelRegistryParams, authInfo runtime.ClientAuthInfoWriter) (*ListModelRegistryOK, *ListModelRegistryNoContent, error) {
	// TODO: Validate the params before sending
	if params == nil {
		params = NewListModelRegistryParams()
	}

	result, err := a.transport.Submit(&runtime.ClientOperation{
		ID:                 "ListModelRegistry",
		Method:             "GET",
		PathPattern:        "/api/v1/orgs/{owner}/models",
		ProducesMediaTypes: []string{"application/json"},
		ConsumesMediaTypes: []string{"application/json"},
		Schemes:            []string{"http", "https"},
		Params:             params,
		Reader:             &ListModelRegistryReader{formats: a.formats},
		AuthInfo:           authInfo,
		Context:            params.Context,
		Client:             params.HTTPClient,
	})
	if err != nil {
		return nil, nil, err
	}
	switch value := result.(type) {
	case *ListModelRegistryOK:
		return value, nil, nil
	case *ListModelRegistryNoContent:
		return nil, value, nil
	}
	// unexpected success response
	unexpectedSuccess := result.(*ListModelRegistryDefault)
	return nil, nil, runtime.NewAPIError("unexpected success response: content available as default response in error", unexpectedSuccess, unexpectedSuccess.Code())
}

/*
  ListModelRegistryNames lists hub model names
*/
func (a *Client) ListModelRegistryNames(params *ListModelRegistryNamesParams, authInfo runtime.ClientAuthInfoWriter) (*ListModelRegistryNamesOK, *ListModelRegistryNamesNoContent, error) {
	// TODO: Validate the params before sending
	if params == nil {
		params = NewListModelRegistryNamesParams()
	}

	result, err := a.transport.Submit(&runtime.ClientOperation{
		ID:                 "ListModelRegistryNames",
		Method:             "GET",
		PathPattern:        "/api/v1/orgs/{owner}/models/names",
		ProducesMediaTypes: []string{"application/json"},
		ConsumesMediaTypes: []string{"application/json"},
		Schemes:            []string{"http", "https"},
		Params:             params,
		Reader:             &ListModelRegistryNamesReader{formats: a.formats},
		AuthInfo:           authInfo,
		Context:            params.Context,
		Client:             params.HTTPClient,
	})
	if err != nil {
		return nil, nil, err
	}
	switch value := result.(type) {
	case *ListModelRegistryNamesOK:
		return value, nil, nil
	case *ListModelRegistryNamesNoContent:
		return nil, value, nil
	}
	// unexpected success response
	unexpectedSuccess := result.(*ListModelRegistryNamesDefault)
	return nil, nil, runtime.NewAPIError("unexpected success response: content available as default response in error", unexpectedSuccess, unexpectedSuccess.Code())
}

/*
  PatchModelRegistry patches hub model
*/
func (a *Client) PatchModelRegistry(params *PatchModelRegistryParams, authInfo runtime.ClientAuthInfoWriter) (*PatchModelRegistryOK, *PatchModelRegistryNoContent, error) {
	// TODO: Validate the params before sending
	if params == nil {
		params = NewPatchModelRegistryParams()
	}

	result, err := a.transport.Submit(&runtime.ClientOperation{
		ID:                 "PatchModelRegistry",
		Method:             "PATCH",
		PathPattern:        "/api/v1/orgs/{owner}/models/{model.uuid}",
		ProducesMediaTypes: []string{"application/json"},
		ConsumesMediaTypes: []string{"application/json"},
		Schemes:            []string{"http", "https"},
		Params:             params,
		Reader:             &PatchModelRegistryReader{formats: a.formats},
		AuthInfo:           authInfo,
		Context:            params.Context,
		Client:             params.HTTPClient,
	})
	if err != nil {
		return nil, nil, err
	}
	switch value := result.(type) {
	case *PatchModelRegistryOK:
		return value, nil, nil
	case *PatchModelRegistryNoContent:
		return nil, value, nil
	}
	// unexpected success response
	unexpectedSuccess := result.(*PatchModelRegistryDefault)
	return nil, nil, runtime.NewAPIError("unexpected success response: content available as default response in error", unexpectedSuccess, unexpectedSuccess.Code())
}

/*
  UpdateModelRegistry updates hub model
*/
func (a *Client) UpdateModelRegistry(params *UpdateModelRegistryParams, authInfo runtime.ClientAuthInfoWriter) (*UpdateModelRegistryOK, *UpdateModelRegistryNoContent, error) {
	// TODO: Validate the params before sending
	if params == nil {
		params = NewUpdateModelRegistryParams()
	}

	result, err := a.transport.Submit(&runtime.ClientOperation{
		ID:                 "UpdateModelRegistry",
		Method:             "PUT",
		PathPattern:        "/api/v1/orgs/{owner}/models/{model.uuid}",
		ProducesMediaTypes: []string{"application/json"},
		ConsumesMediaTypes: []string{"application/json"},
		Schemes:            []string{"http", "https"},
		Params:             params,
		Reader:             &UpdateModelRegistryReader{formats: a.formats},
		AuthInfo:           authInfo,
		Context:            params.Context,
		Client:             params.HTTPClient,
	})
	if err != nil {
		return nil, nil, err
	}
	switch value := result.(type) {
	case *UpdateModelRegistryOK:
		return value, nil, nil
	case *UpdateModelRegistryNoContent:
		return nil, value, nil
	}
	// unexpected success response
	unexpectedSuccess := result.(*UpdateModelRegistryDefault)
	return nil, nil, runtime.NewAPIError("unexpected success response: content available as default response in error", unexpectedSuccess, unexpectedSuccess.Code())
}

// SetTransport changes the transport on the client
func (a *Client) SetTransport(transport runtime.ClientTransport) {
	a.transport = transport
}