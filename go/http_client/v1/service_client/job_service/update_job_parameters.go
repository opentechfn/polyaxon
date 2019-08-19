// Copyright 2019 Polyaxon, Inc.
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

package job_service

// This file was generated by the swagger tool.
// Editing this file might prove futile when you re-run the swagger generate command

import (
	"context"
	"net/http"
	"time"

	"github.com/go-openapi/errors"
	"github.com/go-openapi/runtime"
	cr "github.com/go-openapi/runtime/client"

	strfmt "github.com/go-openapi/strfmt"

	service_model "github.com/polyaxon/polyaxon-sdks/go/http_client/v1/service_model"
)

// NewUpdateJobParams creates a new UpdateJobParams object
// with the default values initialized.
func NewUpdateJobParams() *UpdateJobParams {
	var ()
	return &UpdateJobParams{

		timeout: cr.DefaultTimeout,
	}
}

// NewUpdateJobParamsWithTimeout creates a new UpdateJobParams object
// with the default values initialized, and the ability to set a timeout on a request
func NewUpdateJobParamsWithTimeout(timeout time.Duration) *UpdateJobParams {
	var ()
	return &UpdateJobParams{

		timeout: timeout,
	}
}

// NewUpdateJobParamsWithContext creates a new UpdateJobParams object
// with the default values initialized, and the ability to set a context for a request
func NewUpdateJobParamsWithContext(ctx context.Context) *UpdateJobParams {
	var ()
	return &UpdateJobParams{

		Context: ctx,
	}
}

// NewUpdateJobParamsWithHTTPClient creates a new UpdateJobParams object
// with the default values initialized, and the ability to set a custom HTTPClient for a request
func NewUpdateJobParamsWithHTTPClient(client *http.Client) *UpdateJobParams {
	var ()
	return &UpdateJobParams{
		HTTPClient: client,
	}
}

/*UpdateJobParams contains all the parameters to send to the API endpoint
for the update job operation typically these are written to a http.Request
*/
type UpdateJobParams struct {

	/*Body*/
	Body *service_model.V1JobBodyRequest
	/*JobID
	  Unique integer identifier

	*/
	JobID string
	/*Owner
	  Owner of the namespace

	*/
	Owner string
	/*Project
	  Project where the experiement will be assigned

	*/
	Project string

	timeout    time.Duration
	Context    context.Context
	HTTPClient *http.Client
}

// WithTimeout adds the timeout to the update job params
func (o *UpdateJobParams) WithTimeout(timeout time.Duration) *UpdateJobParams {
	o.SetTimeout(timeout)
	return o
}

// SetTimeout adds the timeout to the update job params
func (o *UpdateJobParams) SetTimeout(timeout time.Duration) {
	o.timeout = timeout
}

// WithContext adds the context to the update job params
func (o *UpdateJobParams) WithContext(ctx context.Context) *UpdateJobParams {
	o.SetContext(ctx)
	return o
}

// SetContext adds the context to the update job params
func (o *UpdateJobParams) SetContext(ctx context.Context) {
	o.Context = ctx
}

// WithHTTPClient adds the HTTPClient to the update job params
func (o *UpdateJobParams) WithHTTPClient(client *http.Client) *UpdateJobParams {
	o.SetHTTPClient(client)
	return o
}

// SetHTTPClient adds the HTTPClient to the update job params
func (o *UpdateJobParams) SetHTTPClient(client *http.Client) {
	o.HTTPClient = client
}

// WithBody adds the body to the update job params
func (o *UpdateJobParams) WithBody(body *service_model.V1JobBodyRequest) *UpdateJobParams {
	o.SetBody(body)
	return o
}

// SetBody adds the body to the update job params
func (o *UpdateJobParams) SetBody(body *service_model.V1JobBodyRequest) {
	o.Body = body
}

// WithJobID adds the jobID to the update job params
func (o *UpdateJobParams) WithJobID(jobID string) *UpdateJobParams {
	o.SetJobID(jobID)
	return o
}

// SetJobID adds the jobId to the update job params
func (o *UpdateJobParams) SetJobID(jobID string) {
	o.JobID = jobID
}

// WithOwner adds the owner to the update job params
func (o *UpdateJobParams) WithOwner(owner string) *UpdateJobParams {
	o.SetOwner(owner)
	return o
}

// SetOwner adds the owner to the update job params
func (o *UpdateJobParams) SetOwner(owner string) {
	o.Owner = owner
}

// WithProject adds the project to the update job params
func (o *UpdateJobParams) WithProject(project string) *UpdateJobParams {
	o.SetProject(project)
	return o
}

// SetProject adds the project to the update job params
func (o *UpdateJobParams) SetProject(project string) {
	o.Project = project
}

// WriteToRequest writes these params to a swagger request
func (o *UpdateJobParams) WriteToRequest(r runtime.ClientRequest, reg strfmt.Registry) error {

	if err := r.SetTimeout(o.timeout); err != nil {
		return err
	}
	var res []error

	if o.Body != nil {
		if err := r.SetBodyParam(o.Body); err != nil {
			return err
		}
	}

	// path param job.id
	if err := r.SetPathParam("job.id", o.JobID); err != nil {
		return err
	}

	// path param owner
	if err := r.SetPathParam("owner", o.Owner); err != nil {
		return err
	}

	// path param project
	if err := r.SetPathParam("project", o.Project); err != nil {
		return err
	}

	if len(res) > 0 {
		return errors.CompositeValidationError(res...)
	}
	return nil
}
