#!/usr/bin/python
#
# Copyright 2019 Polyaxon, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: v1/polyaxon_sdk.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from protoc_gen_swagger.options import annotations_pb2 as protoc__gen__swagger_dot_options_dot_annotations__pb2
from v1 import base_pb2 as v1_dot_base__pb2
from v1 import code_ref_pb2 as v1_dot_code__ref__pb2
from v1 import build_pb2 as v1_dot_build__pb2
from v1 import experiment_pb2 as v1_dot_experiment__pb2
from v1 import job_pb2 as v1_dot_job__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='v1/polyaxon_sdk.proto',
  package='v1',
  syntax='proto3',
  serialized_options=_b('\222A\251\002\022g\n\014Polyaxon sdk\"O\n\014Polyaxon sdk\022)https://github.com/polyaxon/polyaxon-sdks\032\024contact@polyaxon.com2\0061.14.4*\004\001\002\003\0042\020application/json:\020application/jsonR:\n\003403\0223\n1You don\'t have permission to access the resource.R)\n\003404\022\"\n\030Resource does not exist.\022\006\n\004\232\002\001\007Z\037\n\035\n\006ApiKey\022\023\010\002\032\rAuthorization \002b\014\n\n\n\006ApiKey\022\000'),
  serialized_pb=_b('\n\x15v1/polyaxon_sdk.proto\x12\x02v1\x1a\x1cgoogle/api/annotations.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a,protoc-gen-swagger/options/annotations.proto\x1a\rv1/base.proto\x1a\x11v1/code_ref.proto\x1a\x0ev1/build.proto\x1a\x13v1/experiment.proto\x1a\x0cv1/job.proto2\x90\x13\n\x0c\x42uildService\x12\x66\n\nListBuilds\x12\x16.v1.ProjectBodyRequest\x1a\x16.v1.ListBuildsResponse\"(\x82\xd3\xe4\x93\x02\"\x12 /api/v1/{owner}/{project}/builds\x12n\n\x14ListBookmarkedBuilds\x12\x14.v1.OwnerBodyRequest\x1a\x16.v1.ListBuildsResponse\"(\x82\xd3\xe4\x93\x02\"\x12 /api/v1/bookmarks/{owner}/builds\x12k\n\x12ListArchivedBuilds\x12\x14.v1.OwnerBodyRequest\x1a\x16.v1.ListBuildsResponse\"\'\x82\xd3\xe4\x93\x02!\x12\x1f/api/v1/archives/{owner}/builds\x12[\n\x0b\x43reateBuild\x12\x14.v1.BuildBodyRequest\x1a\t.v1.Build\"+\x82\xd3\xe4\x93\x02%\" /api/v1/{owner}/{project}/builds:\x01*\x12^\n\x08GetBuild\x12\x18.v1.OwnedEntityIdRequest\x1a\t.v1.Build\"-\x82\xd3\xe4\x93\x02\'\x12%/api/v1/{owner}/{project}/builds/{id}\x12\x66\n\x0bUpdateBuild\x12\x14.v1.BuildBodyRequest\x1a\t.v1.Build\"6\x82\xd3\xe4\x93\x02\x30\x1a+/api/v1/{owner}/{project}/builds/{build.id}:\x01*\x12\x65\n\nPatchBuild\x12\x14.v1.BuildBodyRequest\x1a\t.v1.Build\"6\x82\xd3\xe4\x93\x02\x30\x32+/api/v1/{owner}/{project}/builds/{build.id}:\x01*\x12n\n\x0b\x44\x65leteBuild\x12\x18.v1.OwnedEntityIdRequest\x1a\x16.google.protobuf.Empty\"-\x82\xd3\xe4\x93\x02\'*%/api/v1/{owner}/{project}/builds/{id}\x12t\n\x0c\x44\x65leteBuilds\x12\x18.v1.OwnedEntityIdRequest\x1a\x16.google.protobuf.Empty\"2\x82\xd3\xe4\x93\x02,*\'/api/v1/{owner}/{project}/builds/delete:\x01*\x12t\n\tStopBuild\x12\x18.v1.OwnedEntityIdRequest\x1a\x16.google.protobuf.Empty\"5\x82\xd3\xe4\x93\x02/\"*/api/v1/{owner}/{project}/builds/{id}/stop:\x01*\x12n\n\nStopBuilds\x12\x16.v1.ProjectBodyRequest\x1a\x16.google.protobuf.Empty\"0\x82\xd3\xe4\x93\x02*\"%/api/v1/{owner}/{project}/builds/stop:\x01*\x12m\n\x0cRestartBuild\x12\x18.v1.OwnedEntityIdRequest\x1a\t.v1.Build\"8\x82\xd3\xe4\x93\x02\x32\"-/api/v1/{owner}/{project}/builds/{id}/restart:\x01*\x12w\n\x0c\x41rchiveBuild\x12\x18.v1.OwnedEntityIdRequest\x1a\x16.google.protobuf.Empty\"5\x82\xd3\xe4\x93\x02/\"-/api/v1/{owner}/{project}/builds/{id}/archive\x12w\n\x0cRestoreBuild\x12\x18.v1.OwnedEntityIdRequest\x1a\x16.google.protobuf.Empty\"5\x82\xd3\xe4\x93\x02/\"-/api/v1/{owner}/{project}/builds/{id}/restore\x12y\n\rBookmarkBuild\x12\x18.v1.OwnedEntityIdRequest\x1a\x16.google.protobuf.Empty\"6\x82\xd3\xe4\x93\x02\x30\"./api/v1/{owner}/{project}/builds/{id}/bookmark\x12}\n\x0fUnBookmarkBuild\x12\x18.v1.OwnedEntityIdRequest\x1a\x16.google.protobuf.Empty\"8\x82\xd3\xe4\x93\x02\x32*0/api/v1/{owner}/{project}/builds/{id}/unbookmark\x12x\n\x10GetBuildStatuses\x12\x18.v1.OwnedEntityIdRequest\x1a\x12.v1.StatusResponse\"6\x82\xd3\xe4\x93\x02\x30\x12./api/v1/{owner}/{project}/builds/{id}/statuses\x12\x84\x01\n\x11ListBuildStatuses\x12\x18.v1.OwnedEntityIdRequest\x1a\x1d.v1.ListBuildStatusesResponse\"6\x82\xd3\xe4\x93\x02\x30\x12./api/v1/{owner}/{project}/builds/{id}/statuses\x12y\n\x11\x43reateBuildStatus\x12\x18.v1.OwnedEntityIdRequest\x1a\x0f.v1.BuildStatus\"9\x82\xd3\xe4\x93\x02\x33\"./api/v1/{owner}/{project}/builds/{id}/statuses:\x01*\x12u\n\x0fGetBuildCodeRef\x12\x18.v1.OwnedEntityIdRequest\x1a\x11.v1.CodeReference\"5\x82\xd3\xe4\x93\x02/\x12-/api/v1/{owner}/{project}/builds/{id}/coderef\x12\x94\x01\n\x12\x43reateBuildCodeRef\x12\x1c.v1.CodeReferenceBodyRequest\x1a\x11.v1.CodeReference\"M\x82\xd3\xe4\x93\x02G\"B/api/v1/{entity.owner}/{entity.project}/builds/{entity.id}/coderef:\x01*2\x82\x13\n\nJobService\x12`\n\x08ListJobs\x12\x16.v1.ProjectBodyRequest\x1a\x14.v1.ListJobsResponse\"&\x82\xd3\xe4\x93\x02 \x12\x1e/api/v1/{owner}/{project}/jobs\x12h\n\x12ListBookmarkedJobs\x12\x14.v1.OwnerBodyRequest\x1a\x14.v1.ListJobsResponse\"&\x82\xd3\xe4\x93\x02 \x12\x1e/api/v1/bookmarks/{owner}/jobs\x12\x65\n\x10ListArchivedJobs\x12\x14.v1.OwnerBodyRequest\x1a\x14.v1.ListJobsResponse\"%\x82\xd3\xe4\x93\x02\x1f\x12\x1d/api/v1/archives/{owner}/jobs\x12S\n\tCreateJob\x12\x12.v1.JobBodyRequest\x1a\x07.v1.Job\")\x82\xd3\xe4\x93\x02#\"\x1e/api/v1/{owner}/{project}/jobs:\x01*\x12X\n\x06GetJob\x12\x18.v1.OwnedEntityIdRequest\x1a\x07.v1.Job\"+\x82\xd3\xe4\x93\x02%\x12#/api/v1/{owner}/{project}/jobs/{id}\x12\\\n\tUpdateJob\x12\x12.v1.JobBodyRequest\x1a\x07.v1.Job\"2\x82\xd3\xe4\x93\x02,\x1a\'/api/v1/{owner}/{project}/jobs/{job.id}:\x01*\x12[\n\x08PatchJob\x12\x12.v1.JobBodyRequest\x1a\x07.v1.Job\"2\x82\xd3\xe4\x93\x02,2\'/api/v1/{owner}/{project}/jobs/{job.id}:\x01*\x12j\n\tDeleteJob\x12\x18.v1.OwnedEntityIdRequest\x1a\x16.google.protobuf.Empty\"+\x82\xd3\xe4\x93\x02%*#/api/v1/{owner}/{project}/jobs/{id}\x12p\n\nDeleteJobs\x12\x18.v1.OwnedEntityIdRequest\x1a\x16.google.protobuf.Empty\"0\x82\xd3\xe4\x93\x02**%/api/v1/{owner}/{project}/jobs/delete:\x01*\x12p\n\x07StopJob\x12\x18.v1.OwnedEntityIdRequest\x1a\x16.google.protobuf.Empty\"3\x82\xd3\xe4\x93\x02-\"(/api/v1/{owner}/{project}/jobs/{id}/stop:\x01*\x12j\n\x08StopJobs\x12\x16.v1.ProjectBodyRequest\x1a\x16.google.protobuf.Empty\".\x82\xd3\xe4\x93\x02(\"#/api/v1/{owner}/{project}/jobs/stop:\x01*\x12g\n\nRestartJob\x12\x18.v1.OwnedEntityIdRequest\x1a\x07.v1.Job\"6\x82\xd3\xe4\x93\x02\x30\"+/api/v1/{owner}/{project}/jobs/{id}/restart:\x01*\x12\x65\n\tResumeJob\x12\x18.v1.OwnedEntityIdRequest\x1a\x07.v1.Job\"5\x82\xd3\xe4\x93\x02/\"*/api/v1/{owner}/{project}/jobs/{id}/resume:\x01*\x12s\n\nArchiveJob\x12\x18.v1.OwnedEntityIdRequest\x1a\x16.google.protobuf.Empty\"3\x82\xd3\xe4\x93\x02-\"+/api/v1/{owner}/{project}/jobs/{id}/archive\x12s\n\nRestoreJob\x12\x18.v1.OwnedEntityIdRequest\x1a\x16.google.protobuf.Empty\"3\x82\xd3\xe4\x93\x02-\"+/api/v1/{owner}/{project}/jobs/{id}/restore\x12u\n\x0b\x42ookmarkJob\x12\x18.v1.OwnedEntityIdRequest\x1a\x16.google.protobuf.Empty\"4\x82\xd3\xe4\x93\x02.\",/api/v1/{owner}/{project}/jobs/{id}/bookmark\x12y\n\rUnBookmarkJob\x12\x18.v1.OwnedEntityIdRequest\x1a\x16.google.protobuf.Empty\"6\x82\xd3\xe4\x93\x02\x30*./api/v1/{owner}/{project}/jobs/{id}/unbookmark\x12t\n\x0eGetJobStatuses\x12\x18.v1.OwnedEntityIdRequest\x1a\x12.v1.StatusResponse\"4\x82\xd3\xe4\x93\x02.\x12,/api/v1/{owner}/{project}/jobs/{id}/statuses\x12~\n\x0fListJobStatuses\x12\x18.v1.OwnedEntityIdRequest\x1a\x1b.v1.ListJobStatusesResponse\"4\x82\xd3\xe4\x93\x02.\x12,/api/v1/{owner}/{project}/jobs/{id}/statuses\x12s\n\x0f\x43reateJobStatus\x12\x18.v1.OwnedEntityIdRequest\x1a\r.v1.JobStatus\"7\x82\xd3\xe4\x93\x02\x31\",/api/v1/{owner}/{project}/jobs/{id}/statuses:\x01*\x12q\n\rGetJobCodeRef\x12\x18.v1.OwnedEntityIdRequest\x1a\x11.v1.CodeReference\"3\x82\xd3\xe4\x93\x02-\x12+/api/v1/{owner}/{project}/jobs/{id}/coderef\x12\x90\x01\n\x10\x43reateJobCodeRef\x12\x1c.v1.CodeReferenceBodyRequest\x1a\x11.v1.CodeReference\"K\x82\xd3\xe4\x93\x02\x45\"@/api/v1/{entity.owner}/{entity.project}/jobs/{entity.id}/coderef:\x01*2\xe3\x18\n\x11\x45xperimentService\x12u\n\x0fListExperiments\x12\x16.v1.ProjectBodyRequest\x1a\x1b.v1.ListExperimentsResponse\"-\x82\xd3\xe4\x93\x02\'\x12%/api/v1/{owner}/{project}/experiments\x12}\n\x19ListBookmarkedExperiments\x12\x14.v1.OwnerBodyRequest\x1a\x1b.v1.ListExperimentsResponse\"-\x82\xd3\xe4\x93\x02\'\x12%/api/v1/bookmarks/{owner}/experiments\x12z\n\x17ListArchivedExperiments\x12\x14.v1.OwnerBodyRequest\x1a\x1b.v1.ListExperimentsResponse\",\x82\xd3\xe4\x93\x02&\x12$/api/v1/archives/{owner}/experiments\x12o\n\x10\x43reateExperiment\x12\x19.v1.ExperimentBodyRequest\x1a\x0e.v1.Experiment\"0\x82\xd3\xe4\x93\x02*\"%/api/v1/{owner}/{project}/experiments:\x01*\x12m\n\rGetExperiment\x12\x18.v1.OwnedEntityIdRequest\x1a\x0e.v1.Experiment\"2\x82\xd3\xe4\x93\x02,\x12*/api/v1/{owner}/{project}/experiments/{id}\x12\x7f\n\x10UpdateExperiment\x12\x19.v1.ExperimentBodyRequest\x1a\x0e.v1.Experiment\"@\x82\xd3\xe4\x93\x02:\x1a\x35/api/v1/{owner}/{project}/experiments/{experiment.id}:\x01*\x12~\n\x0fPatchExperiment\x12\x19.v1.ExperimentBodyRequest\x1a\x0e.v1.Experiment\"@\x82\xd3\xe4\x93\x02:25/api/v1/{owner}/{project}/experiments/{experiment.id}:\x01*\x12x\n\x10\x44\x65leteExperiment\x12\x18.v1.OwnedEntityIdRequest\x1a\x16.google.protobuf.Empty\"2\x82\xd3\xe4\x93\x02,**/api/v1/{owner}/{project}/experiments/{id}\x12~\n\x11\x44\x65leteExperiments\x12\x18.v1.OwnedEntityIdRequest\x1a\x16.google.protobuf.Empty\"7\x82\xd3\xe4\x93\x02\x31*,/api/v1/{owner}/{project}/experiments/delete:\x01*\x12~\n\x0eStopExperiment\x12\x18.v1.OwnedEntityIdRequest\x1a\x16.google.protobuf.Empty\":\x82\xd3\xe4\x93\x02\x34\"//api/v1/{owner}/{project}/experiments/{id}/stop:\x01*\x12x\n\x0fStopExperiments\x12\x16.v1.ProjectBodyRequest\x1a\x16.google.protobuf.Empty\"5\x82\xd3\xe4\x93\x02/\"*/api/v1/{owner}/{project}/experiments/stop:\x01*\x12|\n\x11RestartExperiment\x12\x18.v1.OwnedEntityIdRequest\x1a\x0e.v1.Experiment\"=\x82\xd3\xe4\x93\x02\x37\"2/api/v1/{owner}/{project}/experiments/{id}/restart:\x01*\x12z\n\x10ResumeExperiment\x12\x18.v1.OwnedEntityIdRequest\x1a\x0e.v1.Experiment\"<\x82\xd3\xe4\x93\x02\x36\"1/api/v1/{owner}/{project}/experiments/{id}/resume:\x01*\x12\x81\x01\n\x11\x41rchiveExperiment\x12\x18.v1.OwnedEntityIdRequest\x1a\x16.google.protobuf.Empty\":\x82\xd3\xe4\x93\x02\x34\"2/api/v1/{owner}/{project}/experiments/{id}/archive\x12\x81\x01\n\x11RestoreExperiment\x12\x18.v1.OwnedEntityIdRequest\x1a\x16.google.protobuf.Empty\":\x82\xd3\xe4\x93\x02\x34\"2/api/v1/{owner}/{project}/experiments/{id}/restore\x12\x83\x01\n\x12\x42ookmarkExperiment\x12\x18.v1.OwnedEntityIdRequest\x1a\x16.google.protobuf.Empty\";\x82\xd3\xe4\x93\x02\x35\"3/api/v1/{owner}/{project}/experiments/{id}/bookmark\x12\x87\x01\n\x14UnBookmarkExperiment\x12\x18.v1.OwnedEntityIdRequest\x1a\x16.google.protobuf.Empty\"=\x82\xd3\xe4\x93\x02\x37*5/api/v1/{owner}/{project}/experiments/{id}/unbookmark\x12\x97\x01\n\x1aStartExperimentTensorboard\x12\x18.v1.OwnedEntityIdRequest\x1a\x16.google.protobuf.Empty\"G\x82\xd3\xe4\x93\x02\x41\"</api/v1/{owner}/{project}/experiments/{id}/tensorboard/start:\x01*\x12\x92\x01\n\x19StopExperimentTensorboard\x12\x18.v1.OwnedEntityIdRequest\x1a\x16.google.protobuf.Empty\"C\x82\xd3\xe4\x93\x02=*;/api/v1/{owner}/{project}/experiments/{id}/tensorboard/stop\x12\x82\x01\n\x15GetExperimentStatuses\x12\x18.v1.OwnedEntityIdRequest\x1a\x12.v1.StatusResponse\";\x82\xd3\xe4\x93\x02\x35\x12\x33/api/v1/{owner}/{project}/experiments/{id}/statuses\x12\x93\x01\n\x16ListExperimentStatuses\x12\x18.v1.OwnedEntityIdRequest\x1a\".v1.ListExperimentStatusesResponse\";\x82\xd3\xe4\x93\x02\x35\x12\x33/api/v1/{owner}/{project}/experiments/{id}/statuses\x12\x88\x01\n\x16\x43reateExperimentStatus\x12\x18.v1.OwnedEntityIdRequest\x1a\x14.v1.ExperimentStatus\">\x82\xd3\xe4\x93\x02\x38\"3/api/v1/{owner}/{project}/experiments/{id}/statuses:\x01*\x12\x7f\n\x14GetExperimentCodeRef\x12\x18.v1.OwnedEntityIdRequest\x1a\x11.v1.CodeReference\":\x82\xd3\xe4\x93\x02\x34\x12\x32/api/v1/{owner}/{project}/experiments/{id}/coderef\x12\x9e\x01\n\x17\x43reateExperimentCodeRef\x12\x1c.v1.CodeReferenceBodyRequest\x1a\x11.v1.CodeReference\"R\x82\xd3\xe4\x93\x02L\"G/api/v1/{entity.owner}/{entity.project}/experiments/{entity.id}/coderef:\x01*B\xad\x02\x92\x41\xa9\x02\x12g\n\x0cPolyaxon sdk\"O\n\x0cPolyaxon sdk\x12)https://github.com/polyaxon/polyaxon-sdks\x1a\x14\x63ontact@polyaxon.com2\x06\x31.14.4*\x04\x01\x02\x03\x04\x32\x10\x61pplication/json:\x10\x61pplication/jsonR:\n\x03\x34\x30\x33\x12\x33\n1You don\'t have permission to access the resource.R)\n\x03\x34\x30\x34\x12\"\n\x18Resource does not exist.\x12\x06\n\x04\x9a\x02\x01\x07Z\x1f\n\x1d\n\x06\x41piKey\x12\x13\x08\x02\x1a\rAuthorization \x02\x62\x0c\n\n\n\x06\x41piKey\x12\x00\x62\x06proto3')
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,protoc__gen__swagger_dot_options_dot_annotations__pb2.DESCRIPTOR,v1_dot_base__pb2.DESCRIPTOR,v1_dot_code__ref__pb2.DESCRIPTOR,v1_dot_build__pb2.DESCRIPTOR,v1_dot_experiment__pb2.DESCRIPTOR,v1_dot_job__pb2.DESCRIPTOR,])



_sym_db.RegisterFileDescriptor(DESCRIPTOR)


DESCRIPTOR._options = None

_BUILDSERVICE = _descriptor.ServiceDescriptor(
  name='BuildService',
  full_name='v1.BuildService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=220,
  serialized_end=2668,
  methods=[
  _descriptor.MethodDescriptor(
    name='ListBuilds',
    full_name='v1.BuildService.ListBuilds',
    index=0,
    containing_service=None,
    input_type=v1_dot_base__pb2._PROJECTBODYREQUEST,
    output_type=v1_dot_build__pb2._LISTBUILDSRESPONSE,
    serialized_options=_b('\202\323\344\223\002\"\022 /api/v1/{owner}/{project}/builds'),
  ),
  _descriptor.MethodDescriptor(
    name='ListBookmarkedBuilds',
    full_name='v1.BuildService.ListBookmarkedBuilds',
    index=1,
    containing_service=None,
    input_type=v1_dot_base__pb2._OWNERBODYREQUEST,
    output_type=v1_dot_build__pb2._LISTBUILDSRESPONSE,
    serialized_options=_b('\202\323\344\223\002\"\022 /api/v1/bookmarks/{owner}/builds'),
  ),
  _descriptor.MethodDescriptor(
    name='ListArchivedBuilds',
    full_name='v1.BuildService.ListArchivedBuilds',
    index=2,
    containing_service=None,
    input_type=v1_dot_base__pb2._OWNERBODYREQUEST,
    output_type=v1_dot_build__pb2._LISTBUILDSRESPONSE,
    serialized_options=_b('\202\323\344\223\002!\022\037/api/v1/archives/{owner}/builds'),
  ),
  _descriptor.MethodDescriptor(
    name='CreateBuild',
    full_name='v1.BuildService.CreateBuild',
    index=3,
    containing_service=None,
    input_type=v1_dot_build__pb2._BUILDBODYREQUEST,
    output_type=v1_dot_build__pb2._BUILD,
    serialized_options=_b('\202\323\344\223\002%\" /api/v1/{owner}/{project}/builds:\001*'),
  ),
  _descriptor.MethodDescriptor(
    name='GetBuild',
    full_name='v1.BuildService.GetBuild',
    index=4,
    containing_service=None,
    input_type=v1_dot_base__pb2._OWNEDENTITYIDREQUEST,
    output_type=v1_dot_build__pb2._BUILD,
    serialized_options=_b('\202\323\344\223\002\'\022%/api/v1/{owner}/{project}/builds/{id}'),
  ),
  _descriptor.MethodDescriptor(
    name='UpdateBuild',
    full_name='v1.BuildService.UpdateBuild',
    index=5,
    containing_service=None,
    input_type=v1_dot_build__pb2._BUILDBODYREQUEST,
    output_type=v1_dot_build__pb2._BUILD,
    serialized_options=_b('\202\323\344\223\0020\032+/api/v1/{owner}/{project}/builds/{build.id}:\001*'),
  ),
  _descriptor.MethodDescriptor(
    name='PatchBuild',
    full_name='v1.BuildService.PatchBuild',
    index=6,
    containing_service=None,
    input_type=v1_dot_build__pb2._BUILDBODYREQUEST,
    output_type=v1_dot_build__pb2._BUILD,
    serialized_options=_b('\202\323\344\223\00202+/api/v1/{owner}/{project}/builds/{build.id}:\001*'),
  ),
  _descriptor.MethodDescriptor(
    name='DeleteBuild',
    full_name='v1.BuildService.DeleteBuild',
    index=7,
    containing_service=None,
    input_type=v1_dot_base__pb2._OWNEDENTITYIDREQUEST,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    serialized_options=_b('\202\323\344\223\002\'*%/api/v1/{owner}/{project}/builds/{id}'),
  ),
  _descriptor.MethodDescriptor(
    name='DeleteBuilds',
    full_name='v1.BuildService.DeleteBuilds',
    index=8,
    containing_service=None,
    input_type=v1_dot_base__pb2._OWNEDENTITYIDREQUEST,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    serialized_options=_b('\202\323\344\223\002,*\'/api/v1/{owner}/{project}/builds/delete:\001*'),
  ),
  _descriptor.MethodDescriptor(
    name='StopBuild',
    full_name='v1.BuildService.StopBuild',
    index=9,
    containing_service=None,
    input_type=v1_dot_base__pb2._OWNEDENTITYIDREQUEST,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    serialized_options=_b('\202\323\344\223\002/\"*/api/v1/{owner}/{project}/builds/{id}/stop:\001*'),
  ),
  _descriptor.MethodDescriptor(
    name='StopBuilds',
    full_name='v1.BuildService.StopBuilds',
    index=10,
    containing_service=None,
    input_type=v1_dot_base__pb2._PROJECTBODYREQUEST,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    serialized_options=_b('\202\323\344\223\002*\"%/api/v1/{owner}/{project}/builds/stop:\001*'),
  ),
  _descriptor.MethodDescriptor(
    name='RestartBuild',
    full_name='v1.BuildService.RestartBuild',
    index=11,
    containing_service=None,
    input_type=v1_dot_base__pb2._OWNEDENTITYIDREQUEST,
    output_type=v1_dot_build__pb2._BUILD,
    serialized_options=_b('\202\323\344\223\0022\"-/api/v1/{owner}/{project}/builds/{id}/restart:\001*'),
  ),
  _descriptor.MethodDescriptor(
    name='ArchiveBuild',
    full_name='v1.BuildService.ArchiveBuild',
    index=12,
    containing_service=None,
    input_type=v1_dot_base__pb2._OWNEDENTITYIDREQUEST,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    serialized_options=_b('\202\323\344\223\002/\"-/api/v1/{owner}/{project}/builds/{id}/archive'),
  ),
  _descriptor.MethodDescriptor(
    name='RestoreBuild',
    full_name='v1.BuildService.RestoreBuild',
    index=13,
    containing_service=None,
    input_type=v1_dot_base__pb2._OWNEDENTITYIDREQUEST,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    serialized_options=_b('\202\323\344\223\002/\"-/api/v1/{owner}/{project}/builds/{id}/restore'),
  ),
  _descriptor.MethodDescriptor(
    name='BookmarkBuild',
    full_name='v1.BuildService.BookmarkBuild',
    index=14,
    containing_service=None,
    input_type=v1_dot_base__pb2._OWNEDENTITYIDREQUEST,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    serialized_options=_b('\202\323\344\223\0020\"./api/v1/{owner}/{project}/builds/{id}/bookmark'),
  ),
  _descriptor.MethodDescriptor(
    name='UnBookmarkBuild',
    full_name='v1.BuildService.UnBookmarkBuild',
    index=15,
    containing_service=None,
    input_type=v1_dot_base__pb2._OWNEDENTITYIDREQUEST,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    serialized_options=_b('\202\323\344\223\0022*0/api/v1/{owner}/{project}/builds/{id}/unbookmark'),
  ),
  _descriptor.MethodDescriptor(
    name='GetBuildStatuses',
    full_name='v1.BuildService.GetBuildStatuses',
    index=16,
    containing_service=None,
    input_type=v1_dot_base__pb2._OWNEDENTITYIDREQUEST,
    output_type=v1_dot_base__pb2._STATUSRESPONSE,
    serialized_options=_b('\202\323\344\223\0020\022./api/v1/{owner}/{project}/builds/{id}/statuses'),
  ),
  _descriptor.MethodDescriptor(
    name='ListBuildStatuses',
    full_name='v1.BuildService.ListBuildStatuses',
    index=17,
    containing_service=None,
    input_type=v1_dot_base__pb2._OWNEDENTITYIDREQUEST,
    output_type=v1_dot_build__pb2._LISTBUILDSTATUSESRESPONSE,
    serialized_options=_b('\202\323\344\223\0020\022./api/v1/{owner}/{project}/builds/{id}/statuses'),
  ),
  _descriptor.MethodDescriptor(
    name='CreateBuildStatus',
    full_name='v1.BuildService.CreateBuildStatus',
    index=18,
    containing_service=None,
    input_type=v1_dot_base__pb2._OWNEDENTITYIDREQUEST,
    output_type=v1_dot_build__pb2._BUILDSTATUS,
    serialized_options=_b('\202\323\344\223\0023\"./api/v1/{owner}/{project}/builds/{id}/statuses:\001*'),
  ),
  _descriptor.MethodDescriptor(
    name='GetBuildCodeRef',
    full_name='v1.BuildService.GetBuildCodeRef',
    index=19,
    containing_service=None,
    input_type=v1_dot_base__pb2._OWNEDENTITYIDREQUEST,
    output_type=v1_dot_code__ref__pb2._CODEREFERENCE,
    serialized_options=_b('\202\323\344\223\002/\022-/api/v1/{owner}/{project}/builds/{id}/coderef'),
  ),
  _descriptor.MethodDescriptor(
    name='CreateBuildCodeRef',
    full_name='v1.BuildService.CreateBuildCodeRef',
    index=20,
    containing_service=None,
    input_type=v1_dot_code__ref__pb2._CODEREFERENCEBODYREQUEST,
    output_type=v1_dot_code__ref__pb2._CODEREFERENCE,
    serialized_options=_b('\202\323\344\223\002G\"B/api/v1/{entity.owner}/{entity.project}/builds/{entity.id}/coderef:\001*'),
  ),
])
_sym_db.RegisterServiceDescriptor(_BUILDSERVICE)

DESCRIPTOR.services_by_name['BuildService'] = _BUILDSERVICE


_JOBSERVICE = _descriptor.ServiceDescriptor(
  name='JobService',
  full_name='v1.JobService',
  file=DESCRIPTOR,
  index=1,
  serialized_options=None,
  serialized_start=2671,
  serialized_end=5105,
  methods=[
  _descriptor.MethodDescriptor(
    name='ListJobs',
    full_name='v1.JobService.ListJobs',
    index=0,
    containing_service=None,
    input_type=v1_dot_base__pb2._PROJECTBODYREQUEST,
    output_type=v1_dot_job__pb2._LISTJOBSRESPONSE,
    serialized_options=_b('\202\323\344\223\002 \022\036/api/v1/{owner}/{project}/jobs'),
  ),
  _descriptor.MethodDescriptor(
    name='ListBookmarkedJobs',
    full_name='v1.JobService.ListBookmarkedJobs',
    index=1,
    containing_service=None,
    input_type=v1_dot_base__pb2._OWNERBODYREQUEST,
    output_type=v1_dot_job__pb2._LISTJOBSRESPONSE,
    serialized_options=_b('\202\323\344\223\002 \022\036/api/v1/bookmarks/{owner}/jobs'),
  ),
  _descriptor.MethodDescriptor(
    name='ListArchivedJobs',
    full_name='v1.JobService.ListArchivedJobs',
    index=2,
    containing_service=None,
    input_type=v1_dot_base__pb2._OWNERBODYREQUEST,
    output_type=v1_dot_job__pb2._LISTJOBSRESPONSE,
    serialized_options=_b('\202\323\344\223\002\037\022\035/api/v1/archives/{owner}/jobs'),
  ),
  _descriptor.MethodDescriptor(
    name='CreateJob',
    full_name='v1.JobService.CreateJob',
    index=3,
    containing_service=None,
    input_type=v1_dot_job__pb2._JOBBODYREQUEST,
    output_type=v1_dot_job__pb2._JOB,
    serialized_options=_b('\202\323\344\223\002#\"\036/api/v1/{owner}/{project}/jobs:\001*'),
  ),
  _descriptor.MethodDescriptor(
    name='GetJob',
    full_name='v1.JobService.GetJob',
    index=4,
    containing_service=None,
    input_type=v1_dot_base__pb2._OWNEDENTITYIDREQUEST,
    output_type=v1_dot_job__pb2._JOB,
    serialized_options=_b('\202\323\344\223\002%\022#/api/v1/{owner}/{project}/jobs/{id}'),
  ),
  _descriptor.MethodDescriptor(
    name='UpdateJob',
    full_name='v1.JobService.UpdateJob',
    index=5,
    containing_service=None,
    input_type=v1_dot_job__pb2._JOBBODYREQUEST,
    output_type=v1_dot_job__pb2._JOB,
    serialized_options=_b('\202\323\344\223\002,\032\'/api/v1/{owner}/{project}/jobs/{job.id}:\001*'),
  ),
  _descriptor.MethodDescriptor(
    name='PatchJob',
    full_name='v1.JobService.PatchJob',
    index=6,
    containing_service=None,
    input_type=v1_dot_job__pb2._JOBBODYREQUEST,
    output_type=v1_dot_job__pb2._JOB,
    serialized_options=_b('\202\323\344\223\002,2\'/api/v1/{owner}/{project}/jobs/{job.id}:\001*'),
  ),
  _descriptor.MethodDescriptor(
    name='DeleteJob',
    full_name='v1.JobService.DeleteJob',
    index=7,
    containing_service=None,
    input_type=v1_dot_base__pb2._OWNEDENTITYIDREQUEST,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    serialized_options=_b('\202\323\344\223\002%*#/api/v1/{owner}/{project}/jobs/{id}'),
  ),
  _descriptor.MethodDescriptor(
    name='DeleteJobs',
    full_name='v1.JobService.DeleteJobs',
    index=8,
    containing_service=None,
    input_type=v1_dot_base__pb2._OWNEDENTITYIDREQUEST,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    serialized_options=_b('\202\323\344\223\002**%/api/v1/{owner}/{project}/jobs/delete:\001*'),
  ),
  _descriptor.MethodDescriptor(
    name='StopJob',
    full_name='v1.JobService.StopJob',
    index=9,
    containing_service=None,
    input_type=v1_dot_base__pb2._OWNEDENTITYIDREQUEST,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    serialized_options=_b('\202\323\344\223\002-\"(/api/v1/{owner}/{project}/jobs/{id}/stop:\001*'),
  ),
  _descriptor.MethodDescriptor(
    name='StopJobs',
    full_name='v1.JobService.StopJobs',
    index=10,
    containing_service=None,
    input_type=v1_dot_base__pb2._PROJECTBODYREQUEST,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    serialized_options=_b('\202\323\344\223\002(\"#/api/v1/{owner}/{project}/jobs/stop:\001*'),
  ),
  _descriptor.MethodDescriptor(
    name='RestartJob',
    full_name='v1.JobService.RestartJob',
    index=11,
    containing_service=None,
    input_type=v1_dot_base__pb2._OWNEDENTITYIDREQUEST,
    output_type=v1_dot_job__pb2._JOB,
    serialized_options=_b('\202\323\344\223\0020\"+/api/v1/{owner}/{project}/jobs/{id}/restart:\001*'),
  ),
  _descriptor.MethodDescriptor(
    name='ResumeJob',
    full_name='v1.JobService.ResumeJob',
    index=12,
    containing_service=None,
    input_type=v1_dot_base__pb2._OWNEDENTITYIDREQUEST,
    output_type=v1_dot_job__pb2._JOB,
    serialized_options=_b('\202\323\344\223\002/\"*/api/v1/{owner}/{project}/jobs/{id}/resume:\001*'),
  ),
  _descriptor.MethodDescriptor(
    name='ArchiveJob',
    full_name='v1.JobService.ArchiveJob',
    index=13,
    containing_service=None,
    input_type=v1_dot_base__pb2._OWNEDENTITYIDREQUEST,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    serialized_options=_b('\202\323\344\223\002-\"+/api/v1/{owner}/{project}/jobs/{id}/archive'),
  ),
  _descriptor.MethodDescriptor(
    name='RestoreJob',
    full_name='v1.JobService.RestoreJob',
    index=14,
    containing_service=None,
    input_type=v1_dot_base__pb2._OWNEDENTITYIDREQUEST,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    serialized_options=_b('\202\323\344\223\002-\"+/api/v1/{owner}/{project}/jobs/{id}/restore'),
  ),
  _descriptor.MethodDescriptor(
    name='BookmarkJob',
    full_name='v1.JobService.BookmarkJob',
    index=15,
    containing_service=None,
    input_type=v1_dot_base__pb2._OWNEDENTITYIDREQUEST,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    serialized_options=_b('\202\323\344\223\002.\",/api/v1/{owner}/{project}/jobs/{id}/bookmark'),
  ),
  _descriptor.MethodDescriptor(
    name='UnBookmarkJob',
    full_name='v1.JobService.UnBookmarkJob',
    index=16,
    containing_service=None,
    input_type=v1_dot_base__pb2._OWNEDENTITYIDREQUEST,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    serialized_options=_b('\202\323\344\223\0020*./api/v1/{owner}/{project}/jobs/{id}/unbookmark'),
  ),
  _descriptor.MethodDescriptor(
    name='GetJobStatuses',
    full_name='v1.JobService.GetJobStatuses',
    index=17,
    containing_service=None,
    input_type=v1_dot_base__pb2._OWNEDENTITYIDREQUEST,
    output_type=v1_dot_base__pb2._STATUSRESPONSE,
    serialized_options=_b('\202\323\344\223\002.\022,/api/v1/{owner}/{project}/jobs/{id}/statuses'),
  ),
  _descriptor.MethodDescriptor(
    name='ListJobStatuses',
    full_name='v1.JobService.ListJobStatuses',
    index=18,
    containing_service=None,
    input_type=v1_dot_base__pb2._OWNEDENTITYIDREQUEST,
    output_type=v1_dot_job__pb2._LISTJOBSTATUSESRESPONSE,
    serialized_options=_b('\202\323\344\223\002.\022,/api/v1/{owner}/{project}/jobs/{id}/statuses'),
  ),
  _descriptor.MethodDescriptor(
    name='CreateJobStatus',
    full_name='v1.JobService.CreateJobStatus',
    index=19,
    containing_service=None,
    input_type=v1_dot_base__pb2._OWNEDENTITYIDREQUEST,
    output_type=v1_dot_job__pb2._JOBSTATUS,
    serialized_options=_b('\202\323\344\223\0021\",/api/v1/{owner}/{project}/jobs/{id}/statuses:\001*'),
  ),
  _descriptor.MethodDescriptor(
    name='GetJobCodeRef',
    full_name='v1.JobService.GetJobCodeRef',
    index=20,
    containing_service=None,
    input_type=v1_dot_base__pb2._OWNEDENTITYIDREQUEST,
    output_type=v1_dot_code__ref__pb2._CODEREFERENCE,
    serialized_options=_b('\202\323\344\223\002-\022+/api/v1/{owner}/{project}/jobs/{id}/coderef'),
  ),
  _descriptor.MethodDescriptor(
    name='CreateJobCodeRef',
    full_name='v1.JobService.CreateJobCodeRef',
    index=21,
    containing_service=None,
    input_type=v1_dot_code__ref__pb2._CODEREFERENCEBODYREQUEST,
    output_type=v1_dot_code__ref__pb2._CODEREFERENCE,
    serialized_options=_b('\202\323\344\223\002E\"@/api/v1/{entity.owner}/{entity.project}/jobs/{entity.id}/coderef:\001*'),
  ),
])
_sym_db.RegisterServiceDescriptor(_JOBSERVICE)

DESCRIPTOR.services_by_name['JobService'] = _JOBSERVICE


_EXPERIMENTSERVICE = _descriptor.ServiceDescriptor(
  name='ExperimentService',
  full_name='v1.ExperimentService',
  file=DESCRIPTOR,
  index=2,
  serialized_options=None,
  serialized_start=5108,
  serialized_end=8279,
  methods=[
  _descriptor.MethodDescriptor(
    name='ListExperiments',
    full_name='v1.ExperimentService.ListExperiments',
    index=0,
    containing_service=None,
    input_type=v1_dot_base__pb2._PROJECTBODYREQUEST,
    output_type=v1_dot_experiment__pb2._LISTEXPERIMENTSRESPONSE,
    serialized_options=_b('\202\323\344\223\002\'\022%/api/v1/{owner}/{project}/experiments'),
  ),
  _descriptor.MethodDescriptor(
    name='ListBookmarkedExperiments',
    full_name='v1.ExperimentService.ListBookmarkedExperiments',
    index=1,
    containing_service=None,
    input_type=v1_dot_base__pb2._OWNERBODYREQUEST,
    output_type=v1_dot_experiment__pb2._LISTEXPERIMENTSRESPONSE,
    serialized_options=_b('\202\323\344\223\002\'\022%/api/v1/bookmarks/{owner}/experiments'),
  ),
  _descriptor.MethodDescriptor(
    name='ListArchivedExperiments',
    full_name='v1.ExperimentService.ListArchivedExperiments',
    index=2,
    containing_service=None,
    input_type=v1_dot_base__pb2._OWNERBODYREQUEST,
    output_type=v1_dot_experiment__pb2._LISTEXPERIMENTSRESPONSE,
    serialized_options=_b('\202\323\344\223\002&\022$/api/v1/archives/{owner}/experiments'),
  ),
  _descriptor.MethodDescriptor(
    name='CreateExperiment',
    full_name='v1.ExperimentService.CreateExperiment',
    index=3,
    containing_service=None,
    input_type=v1_dot_experiment__pb2._EXPERIMENTBODYREQUEST,
    output_type=v1_dot_experiment__pb2._EXPERIMENT,
    serialized_options=_b('\202\323\344\223\002*\"%/api/v1/{owner}/{project}/experiments:\001*'),
  ),
  _descriptor.MethodDescriptor(
    name='GetExperiment',
    full_name='v1.ExperimentService.GetExperiment',
    index=4,
    containing_service=None,
    input_type=v1_dot_base__pb2._OWNEDENTITYIDREQUEST,
    output_type=v1_dot_experiment__pb2._EXPERIMENT,
    serialized_options=_b('\202\323\344\223\002,\022*/api/v1/{owner}/{project}/experiments/{id}'),
  ),
  _descriptor.MethodDescriptor(
    name='UpdateExperiment',
    full_name='v1.ExperimentService.UpdateExperiment',
    index=5,
    containing_service=None,
    input_type=v1_dot_experiment__pb2._EXPERIMENTBODYREQUEST,
    output_type=v1_dot_experiment__pb2._EXPERIMENT,
    serialized_options=_b('\202\323\344\223\002:\0325/api/v1/{owner}/{project}/experiments/{experiment.id}:\001*'),
  ),
  _descriptor.MethodDescriptor(
    name='PatchExperiment',
    full_name='v1.ExperimentService.PatchExperiment',
    index=6,
    containing_service=None,
    input_type=v1_dot_experiment__pb2._EXPERIMENTBODYREQUEST,
    output_type=v1_dot_experiment__pb2._EXPERIMENT,
    serialized_options=_b('\202\323\344\223\002:25/api/v1/{owner}/{project}/experiments/{experiment.id}:\001*'),
  ),
  _descriptor.MethodDescriptor(
    name='DeleteExperiment',
    full_name='v1.ExperimentService.DeleteExperiment',
    index=7,
    containing_service=None,
    input_type=v1_dot_base__pb2._OWNEDENTITYIDREQUEST,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    serialized_options=_b('\202\323\344\223\002,**/api/v1/{owner}/{project}/experiments/{id}'),
  ),
  _descriptor.MethodDescriptor(
    name='DeleteExperiments',
    full_name='v1.ExperimentService.DeleteExperiments',
    index=8,
    containing_service=None,
    input_type=v1_dot_base__pb2._OWNEDENTITYIDREQUEST,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    serialized_options=_b('\202\323\344\223\0021*,/api/v1/{owner}/{project}/experiments/delete:\001*'),
  ),
  _descriptor.MethodDescriptor(
    name='StopExperiment',
    full_name='v1.ExperimentService.StopExperiment',
    index=9,
    containing_service=None,
    input_type=v1_dot_base__pb2._OWNEDENTITYIDREQUEST,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    serialized_options=_b('\202\323\344\223\0024\"//api/v1/{owner}/{project}/experiments/{id}/stop:\001*'),
  ),
  _descriptor.MethodDescriptor(
    name='StopExperiments',
    full_name='v1.ExperimentService.StopExperiments',
    index=10,
    containing_service=None,
    input_type=v1_dot_base__pb2._PROJECTBODYREQUEST,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    serialized_options=_b('\202\323\344\223\002/\"*/api/v1/{owner}/{project}/experiments/stop:\001*'),
  ),
  _descriptor.MethodDescriptor(
    name='RestartExperiment',
    full_name='v1.ExperimentService.RestartExperiment',
    index=11,
    containing_service=None,
    input_type=v1_dot_base__pb2._OWNEDENTITYIDREQUEST,
    output_type=v1_dot_experiment__pb2._EXPERIMENT,
    serialized_options=_b('\202\323\344\223\0027\"2/api/v1/{owner}/{project}/experiments/{id}/restart:\001*'),
  ),
  _descriptor.MethodDescriptor(
    name='ResumeExperiment',
    full_name='v1.ExperimentService.ResumeExperiment',
    index=12,
    containing_service=None,
    input_type=v1_dot_base__pb2._OWNEDENTITYIDREQUEST,
    output_type=v1_dot_experiment__pb2._EXPERIMENT,
    serialized_options=_b('\202\323\344\223\0026\"1/api/v1/{owner}/{project}/experiments/{id}/resume:\001*'),
  ),
  _descriptor.MethodDescriptor(
    name='ArchiveExperiment',
    full_name='v1.ExperimentService.ArchiveExperiment',
    index=13,
    containing_service=None,
    input_type=v1_dot_base__pb2._OWNEDENTITYIDREQUEST,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    serialized_options=_b('\202\323\344\223\0024\"2/api/v1/{owner}/{project}/experiments/{id}/archive'),
  ),
  _descriptor.MethodDescriptor(
    name='RestoreExperiment',
    full_name='v1.ExperimentService.RestoreExperiment',
    index=14,
    containing_service=None,
    input_type=v1_dot_base__pb2._OWNEDENTITYIDREQUEST,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    serialized_options=_b('\202\323\344\223\0024\"2/api/v1/{owner}/{project}/experiments/{id}/restore'),
  ),
  _descriptor.MethodDescriptor(
    name='BookmarkExperiment',
    full_name='v1.ExperimentService.BookmarkExperiment',
    index=15,
    containing_service=None,
    input_type=v1_dot_base__pb2._OWNEDENTITYIDREQUEST,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    serialized_options=_b('\202\323\344\223\0025\"3/api/v1/{owner}/{project}/experiments/{id}/bookmark'),
  ),
  _descriptor.MethodDescriptor(
    name='UnBookmarkExperiment',
    full_name='v1.ExperimentService.UnBookmarkExperiment',
    index=16,
    containing_service=None,
    input_type=v1_dot_base__pb2._OWNEDENTITYIDREQUEST,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    serialized_options=_b('\202\323\344\223\0027*5/api/v1/{owner}/{project}/experiments/{id}/unbookmark'),
  ),
  _descriptor.MethodDescriptor(
    name='StartExperimentTensorboard',
    full_name='v1.ExperimentService.StartExperimentTensorboard',
    index=17,
    containing_service=None,
    input_type=v1_dot_base__pb2._OWNEDENTITYIDREQUEST,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    serialized_options=_b('\202\323\344\223\002A\"</api/v1/{owner}/{project}/experiments/{id}/tensorboard/start:\001*'),
  ),
  _descriptor.MethodDescriptor(
    name='StopExperimentTensorboard',
    full_name='v1.ExperimentService.StopExperimentTensorboard',
    index=18,
    containing_service=None,
    input_type=v1_dot_base__pb2._OWNEDENTITYIDREQUEST,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    serialized_options=_b('\202\323\344\223\002=*;/api/v1/{owner}/{project}/experiments/{id}/tensorboard/stop'),
  ),
  _descriptor.MethodDescriptor(
    name='GetExperimentStatuses',
    full_name='v1.ExperimentService.GetExperimentStatuses',
    index=19,
    containing_service=None,
    input_type=v1_dot_base__pb2._OWNEDENTITYIDREQUEST,
    output_type=v1_dot_base__pb2._STATUSRESPONSE,
    serialized_options=_b('\202\323\344\223\0025\0223/api/v1/{owner}/{project}/experiments/{id}/statuses'),
  ),
  _descriptor.MethodDescriptor(
    name='ListExperimentStatuses',
    full_name='v1.ExperimentService.ListExperimentStatuses',
    index=20,
    containing_service=None,
    input_type=v1_dot_base__pb2._OWNEDENTITYIDREQUEST,
    output_type=v1_dot_experiment__pb2._LISTEXPERIMENTSTATUSESRESPONSE,
    serialized_options=_b('\202\323\344\223\0025\0223/api/v1/{owner}/{project}/experiments/{id}/statuses'),
  ),
  _descriptor.MethodDescriptor(
    name='CreateExperimentStatus',
    full_name='v1.ExperimentService.CreateExperimentStatus',
    index=21,
    containing_service=None,
    input_type=v1_dot_base__pb2._OWNEDENTITYIDREQUEST,
    output_type=v1_dot_experiment__pb2._EXPERIMENTSTATUS,
    serialized_options=_b('\202\323\344\223\0028\"3/api/v1/{owner}/{project}/experiments/{id}/statuses:\001*'),
  ),
  _descriptor.MethodDescriptor(
    name='GetExperimentCodeRef',
    full_name='v1.ExperimentService.GetExperimentCodeRef',
    index=22,
    containing_service=None,
    input_type=v1_dot_base__pb2._OWNEDENTITYIDREQUEST,
    output_type=v1_dot_code__ref__pb2._CODEREFERENCE,
    serialized_options=_b('\202\323\344\223\0024\0222/api/v1/{owner}/{project}/experiments/{id}/coderef'),
  ),
  _descriptor.MethodDescriptor(
    name='CreateExperimentCodeRef',
    full_name='v1.ExperimentService.CreateExperimentCodeRef',
    index=23,
    containing_service=None,
    input_type=v1_dot_code__ref__pb2._CODEREFERENCEBODYREQUEST,
    output_type=v1_dot_code__ref__pb2._CODEREFERENCE,
    serialized_options=_b('\202\323\344\223\002L\"G/api/v1/{entity.owner}/{entity.project}/experiments/{entity.id}/coderef:\001*'),
  ),
])
_sym_db.RegisterServiceDescriptor(_EXPERIMENTSERVICE)

DESCRIPTOR.services_by_name['ExperimentService'] = _EXPERIMENTSERVICE

# @@protoc_insertion_point(module_scope)
