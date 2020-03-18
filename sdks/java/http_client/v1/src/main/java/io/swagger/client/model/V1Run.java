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

/*
 * Polyaxon SDKs and REST API specification.
 * Polyaxon SDKs and REST API specification.
 *
 * OpenAPI spec version: 1.0.5
 * Contact: contact@polyaxon.com
 *
 * NOTE: This class is auto generated by the swagger code generator program.
 * https://github.com/swagger-api/swagger-codegen.git
 * Do not edit the class manually.
 */


package io.swagger.client.model;

import java.util.Objects;
import java.util.Arrays;
import com.google.gson.TypeAdapter;
import com.google.gson.annotations.JsonAdapter;
import com.google.gson.annotations.SerializedName;
import com.google.gson.stream.JsonReader;
import com.google.gson.stream.JsonWriter;
import io.swagger.annotations.ApiModel;
import io.swagger.annotations.ApiModelProperty;
import io.swagger.client.model.V1Cloning;
import io.swagger.client.model.V1Pipeline;
import io.swagger.client.model.V1RunKind;
import io.swagger.client.model.V1StatusCondition;
import io.swagger.client.model.V1Statuses;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;
import org.threeten.bp.OffsetDateTime;

/**
 * V1Run
 */

public class V1Run {
  @SerializedName("uuid")
  private String uuid = null;

  @SerializedName("name")
  private String name = null;

  @SerializedName("description")
  private String description = null;

  @SerializedName("tags")
  private List<String> tags = null;

  @SerializedName("deleted")
  private Boolean deleted = null;

  @SerializedName("user")
  private String user = null;

  @SerializedName("owner")
  private String owner = null;

  @SerializedName("project")
  private String project = null;

  @SerializedName("created_at")
  private OffsetDateTime createdAt = null;

  @SerializedName("updated_at")
  private OffsetDateTime updatedAt = null;

  @SerializedName("started_at")
  private OffsetDateTime startedAt = null;

  @SerializedName("finished_at")
  private OffsetDateTime finishedAt = null;

  @SerializedName("run_time")
  private Integer runTime = null;

  @SerializedName("is_managed")
  private String isManaged = null;

  @SerializedName("content")
  private String content = null;

  @SerializedName("status")
  private V1Statuses status = null;

  @SerializedName("bookmarked")
  private Boolean bookmarked = null;

  @SerializedName("meta_info")
  private Object metaInfo = null;

  @SerializedName("is_helper")
  private Boolean isHelper = null;

  @SerializedName("kind")
  private V1RunKind kind = null;

  @SerializedName("meta_kind")
  private V1RunKind metaKind = null;

  @SerializedName("hub")
  private String hub = null;

  @SerializedName("inputs")
  private Object inputs = null;

  @SerializedName("outputs")
  private Object outputs = null;

  @SerializedName("original")
  private V1Cloning original = null;

  @SerializedName("pipeline")
  private V1Pipeline pipeline = null;

  @SerializedName("status_conditions")
  private List<V1StatusCondition> statusConditions = null;

  public V1Run uuid(String uuid) {
    this.uuid = uuid;
    return this;
  }

   /**
   * Get uuid
   * @return uuid
  **/
  @ApiModelProperty(value = "")
  public String getUuid() {
    return uuid;
  }

  public void setUuid(String uuid) {
    this.uuid = uuid;
  }

  public V1Run name(String name) {
    this.name = name;
    return this;
  }

   /**
   * Get name
   * @return name
  **/
  @ApiModelProperty(value = "")
  public String getName() {
    return name;
  }

  public void setName(String name) {
    this.name = name;
  }

  public V1Run description(String description) {
    this.description = description;
    return this;
  }

   /**
   * Get description
   * @return description
  **/
  @ApiModelProperty(value = "")
  public String getDescription() {
    return description;
  }

  public void setDescription(String description) {
    this.description = description;
  }

  public V1Run tags(List<String> tags) {
    this.tags = tags;
    return this;
  }

  public V1Run addTagsItem(String tagsItem) {
    if (this.tags == null) {
      this.tags = new ArrayList<String>();
    }
    this.tags.add(tagsItem);
    return this;
  }

   /**
   * Get tags
   * @return tags
  **/
  @ApiModelProperty(value = "")
  public List<String> getTags() {
    return tags;
  }

  public void setTags(List<String> tags) {
    this.tags = tags;
  }

  public V1Run deleted(Boolean deleted) {
    this.deleted = deleted;
    return this;
  }

   /**
   * Get deleted
   * @return deleted
  **/
  @ApiModelProperty(value = "")
  public Boolean isDeleted() {
    return deleted;
  }

  public void setDeleted(Boolean deleted) {
    this.deleted = deleted;
  }

  public V1Run user(String user) {
    this.user = user;
    return this;
  }

   /**
   * Get user
   * @return user
  **/
  @ApiModelProperty(value = "")
  public String getUser() {
    return user;
  }

  public void setUser(String user) {
    this.user = user;
  }

  public V1Run owner(String owner) {
    this.owner = owner;
    return this;
  }

   /**
   * Get owner
   * @return owner
  **/
  @ApiModelProperty(value = "")
  public String getOwner() {
    return owner;
  }

  public void setOwner(String owner) {
    this.owner = owner;
  }

  public V1Run project(String project) {
    this.project = project;
    return this;
  }

   /**
   * Get project
   * @return project
  **/
  @ApiModelProperty(value = "")
  public String getProject() {
    return project;
  }

  public void setProject(String project) {
    this.project = project;
  }

  public V1Run createdAt(OffsetDateTime createdAt) {
    this.createdAt = createdAt;
    return this;
  }

   /**
   * Get createdAt
   * @return createdAt
  **/
  @ApiModelProperty(value = "")
  public OffsetDateTime getCreatedAt() {
    return createdAt;
  }

  public void setCreatedAt(OffsetDateTime createdAt) {
    this.createdAt = createdAt;
  }

  public V1Run updatedAt(OffsetDateTime updatedAt) {
    this.updatedAt = updatedAt;
    return this;
  }

   /**
   * Get updatedAt
   * @return updatedAt
  **/
  @ApiModelProperty(value = "")
  public OffsetDateTime getUpdatedAt() {
    return updatedAt;
  }

  public void setUpdatedAt(OffsetDateTime updatedAt) {
    this.updatedAt = updatedAt;
  }

  public V1Run startedAt(OffsetDateTime startedAt) {
    this.startedAt = startedAt;
    return this;
  }

   /**
   * Get startedAt
   * @return startedAt
  **/
  @ApiModelProperty(value = "")
  public OffsetDateTime getStartedAt() {
    return startedAt;
  }

  public void setStartedAt(OffsetDateTime startedAt) {
    this.startedAt = startedAt;
  }

  public V1Run finishedAt(OffsetDateTime finishedAt) {
    this.finishedAt = finishedAt;
    return this;
  }

   /**
   * Get finishedAt
   * @return finishedAt
  **/
  @ApiModelProperty(value = "")
  public OffsetDateTime getFinishedAt() {
    return finishedAt;
  }

  public void setFinishedAt(OffsetDateTime finishedAt) {
    this.finishedAt = finishedAt;
  }

  public V1Run runTime(Integer runTime) {
    this.runTime = runTime;
    return this;
  }

   /**
   * Get runTime
   * @return runTime
  **/
  @ApiModelProperty(value = "")
  public Integer getRunTime() {
    return runTime;
  }

  public void setRunTime(Integer runTime) {
    this.runTime = runTime;
  }

  public V1Run isManaged(String isManaged) {
    this.isManaged = isManaged;
    return this;
  }

   /**
   * Get isManaged
   * @return isManaged
  **/
  @ApiModelProperty(value = "")
  public String getIsManaged() {
    return isManaged;
  }

  public void setIsManaged(String isManaged) {
    this.isManaged = isManaged;
  }

  public V1Run content(String content) {
    this.content = content;
    return this;
  }

   /**
   * Get content
   * @return content
  **/
  @ApiModelProperty(value = "")
  public String getContent() {
    return content;
  }

  public void setContent(String content) {
    this.content = content;
  }

  public V1Run status(V1Statuses status) {
    this.status = status;
    return this;
  }

   /**
   * Get status
   * @return status
  **/
  @ApiModelProperty(value = "")
  public V1Statuses getStatus() {
    return status;
  }

  public void setStatus(V1Statuses status) {
    this.status = status;
  }

  public V1Run bookmarked(Boolean bookmarked) {
    this.bookmarked = bookmarked;
    return this;
  }

   /**
   * Get bookmarked
   * @return bookmarked
  **/
  @ApiModelProperty(value = "")
  public Boolean isBookmarked() {
    return bookmarked;
  }

  public void setBookmarked(Boolean bookmarked) {
    this.bookmarked = bookmarked;
  }

  public V1Run metaInfo(Object metaInfo) {
    this.metaInfo = metaInfo;
    return this;
  }

   /**
   * Get metaInfo
   * @return metaInfo
  **/
  @ApiModelProperty(value = "")
  public Object getMetaInfo() {
    return metaInfo;
  }

  public void setMetaInfo(Object metaInfo) {
    this.metaInfo = metaInfo;
  }

  public V1Run isHelper(Boolean isHelper) {
    this.isHelper = isHelper;
    return this;
  }

   /**
   * Get isHelper
   * @return isHelper
  **/
  @ApiModelProperty(value = "")
  public Boolean isIsHelper() {
    return isHelper;
  }

  public void setIsHelper(Boolean isHelper) {
    this.isHelper = isHelper;
  }

  public V1Run kind(V1RunKind kind) {
    this.kind = kind;
    return this;
  }

   /**
   * Get kind
   * @return kind
  **/
  @ApiModelProperty(value = "")
  public V1RunKind getKind() {
    return kind;
  }

  public void setKind(V1RunKind kind) {
    this.kind = kind;
  }

  public V1Run metaKind(V1RunKind metaKind) {
    this.metaKind = metaKind;
    return this;
  }

   /**
   * Get metaKind
   * @return metaKind
  **/
  @ApiModelProperty(value = "")
  public V1RunKind getMetaKind() {
    return metaKind;
  }

  public void setMetaKind(V1RunKind metaKind) {
    this.metaKind = metaKind;
  }

  public V1Run hub(String hub) {
    this.hub = hub;
    return this;
  }

   /**
   * Get hub
   * @return hub
  **/
  @ApiModelProperty(value = "")
  public String getHub() {
    return hub;
  }

  public void setHub(String hub) {
    this.hub = hub;
  }

  public V1Run inputs(Object inputs) {
    this.inputs = inputs;
    return this;
  }

   /**
   * Get inputs
   * @return inputs
  **/
  @ApiModelProperty(value = "")
  public Object getInputs() {
    return inputs;
  }

  public void setInputs(Object inputs) {
    this.inputs = inputs;
  }

  public V1Run outputs(Object outputs) {
    this.outputs = outputs;
    return this;
  }

   /**
   * Get outputs
   * @return outputs
  **/
  @ApiModelProperty(value = "")
  public Object getOutputs() {
    return outputs;
  }

  public void setOutputs(Object outputs) {
    this.outputs = outputs;
  }

  public V1Run original(V1Cloning original) {
    this.original = original;
    return this;
  }

   /**
   * Get original
   * @return original
  **/
  @ApiModelProperty(value = "")
  public V1Cloning getOriginal() {
    return original;
  }

  public void setOriginal(V1Cloning original) {
    this.original = original;
  }

  public V1Run pipeline(V1Pipeline pipeline) {
    this.pipeline = pipeline;
    return this;
  }

   /**
   * Get pipeline
   * @return pipeline
  **/
  @ApiModelProperty(value = "")
  public V1Pipeline getPipeline() {
    return pipeline;
  }

  public void setPipeline(V1Pipeline pipeline) {
    this.pipeline = pipeline;
  }

  public V1Run statusConditions(List<V1StatusCondition> statusConditions) {
    this.statusConditions = statusConditions;
    return this;
  }

  public V1Run addStatusConditionsItem(V1StatusCondition statusConditionsItem) {
    if (this.statusConditions == null) {
      this.statusConditions = new ArrayList<V1StatusCondition>();
    }
    this.statusConditions.add(statusConditionsItem);
    return this;
  }

   /**
   * Get statusConditions
   * @return statusConditions
  **/
  @ApiModelProperty(value = "")
  public List<V1StatusCondition> getStatusConditions() {
    return statusConditions;
  }

  public void setStatusConditions(List<V1StatusCondition> statusConditions) {
    this.statusConditions = statusConditions;
  }


  @Override
  public boolean equals(java.lang.Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    V1Run v1Run = (V1Run) o;
    return Objects.equals(this.uuid, v1Run.uuid) &&
        Objects.equals(this.name, v1Run.name) &&
        Objects.equals(this.description, v1Run.description) &&
        Objects.equals(this.tags, v1Run.tags) &&
        Objects.equals(this.deleted, v1Run.deleted) &&
        Objects.equals(this.user, v1Run.user) &&
        Objects.equals(this.owner, v1Run.owner) &&
        Objects.equals(this.project, v1Run.project) &&
        Objects.equals(this.createdAt, v1Run.createdAt) &&
        Objects.equals(this.updatedAt, v1Run.updatedAt) &&
        Objects.equals(this.startedAt, v1Run.startedAt) &&
        Objects.equals(this.finishedAt, v1Run.finishedAt) &&
        Objects.equals(this.runTime, v1Run.runTime) &&
        Objects.equals(this.isManaged, v1Run.isManaged) &&
        Objects.equals(this.content, v1Run.content) &&
        Objects.equals(this.status, v1Run.status) &&
        Objects.equals(this.bookmarked, v1Run.bookmarked) &&
        Objects.equals(this.metaInfo, v1Run.metaInfo) &&
        Objects.equals(this.isHelper, v1Run.isHelper) &&
        Objects.equals(this.kind, v1Run.kind) &&
        Objects.equals(this.metaKind, v1Run.metaKind) &&
        Objects.equals(this.hub, v1Run.hub) &&
        Objects.equals(this.inputs, v1Run.inputs) &&
        Objects.equals(this.outputs, v1Run.outputs) &&
        Objects.equals(this.original, v1Run.original) &&
        Objects.equals(this.pipeline, v1Run.pipeline) &&
        Objects.equals(this.statusConditions, v1Run.statusConditions);
  }

  @Override
  public int hashCode() {
    return Objects.hash(uuid, name, description, tags, deleted, user, owner, project, createdAt, updatedAt, startedAt, finishedAt, runTime, isManaged, content, status, bookmarked, metaInfo, isHelper, kind, metaKind, hub, inputs, outputs, original, pipeline, statusConditions);
  }


  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class V1Run {\n");
    
    sb.append("    uuid: ").append(toIndentedString(uuid)).append("\n");
    sb.append("    name: ").append(toIndentedString(name)).append("\n");
    sb.append("    description: ").append(toIndentedString(description)).append("\n");
    sb.append("    tags: ").append(toIndentedString(tags)).append("\n");
    sb.append("    deleted: ").append(toIndentedString(deleted)).append("\n");
    sb.append("    user: ").append(toIndentedString(user)).append("\n");
    sb.append("    owner: ").append(toIndentedString(owner)).append("\n");
    sb.append("    project: ").append(toIndentedString(project)).append("\n");
    sb.append("    createdAt: ").append(toIndentedString(createdAt)).append("\n");
    sb.append("    updatedAt: ").append(toIndentedString(updatedAt)).append("\n");
    sb.append("    startedAt: ").append(toIndentedString(startedAt)).append("\n");
    sb.append("    finishedAt: ").append(toIndentedString(finishedAt)).append("\n");
    sb.append("    runTime: ").append(toIndentedString(runTime)).append("\n");
    sb.append("    isManaged: ").append(toIndentedString(isManaged)).append("\n");
    sb.append("    content: ").append(toIndentedString(content)).append("\n");
    sb.append("    status: ").append(toIndentedString(status)).append("\n");
    sb.append("    bookmarked: ").append(toIndentedString(bookmarked)).append("\n");
    sb.append("    metaInfo: ").append(toIndentedString(metaInfo)).append("\n");
    sb.append("    isHelper: ").append(toIndentedString(isHelper)).append("\n");
    sb.append("    kind: ").append(toIndentedString(kind)).append("\n");
    sb.append("    metaKind: ").append(toIndentedString(metaKind)).append("\n");
    sb.append("    hub: ").append(toIndentedString(hub)).append("\n");
    sb.append("    inputs: ").append(toIndentedString(inputs)).append("\n");
    sb.append("    outputs: ").append(toIndentedString(outputs)).append("\n");
    sb.append("    original: ").append(toIndentedString(original)).append("\n");
    sb.append("    pipeline: ").append(toIndentedString(pipeline)).append("\n");
    sb.append("    statusConditions: ").append(toIndentedString(statusConditions)).append("\n");
    sb.append("}");
    return sb.toString();
  }

  /**
   * Convert the given object to string with each line indented by 4 spaces
   * (except the first line).
   */
  private String toIndentedString(java.lang.Object o) {
    if (o == null) {
      return "null";
    }
    return o.toString().replace("\n", "\n    ");
  }

}

