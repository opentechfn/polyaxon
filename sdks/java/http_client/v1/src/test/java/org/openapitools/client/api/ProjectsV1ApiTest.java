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
 * The version of the OpenAPI document: 1.1.8-rc0
 * Contact: contact@polyaxon.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */


package org.openapitools.client.api;

import org.openapitools.client.ApiException;
import java.io.File;
import org.openapitools.client.model.RuntimeError;
import org.openapitools.client.model.V1ListBookmarksResponse;
import org.openapitools.client.model.V1ListProjectsResponse;
import org.openapitools.client.model.V1Project;
import org.openapitools.client.model.V1ProjectSettings;
import org.openapitools.client.model.V1ProjectTeams;
import org.junit.Test;
import org.junit.Ignore;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * API tests for ProjectsV1Api
 */
@Ignore
public class ProjectsV1ApiTest {

    private final ProjectsV1Api api = new ProjectsV1Api();

    
    /**
     * Archive project
     *
     * 
     *
     * @throws ApiException
     *          if the Api call fails
     */
    @Test
    public void archiveProjectTest() throws ApiException {
        String owner = null;
        String project = null;
        api.archiveProject(owner, project);

        // TODO: test validations
    }
    
    /**
     * Bookmark project
     *
     * 
     *
     * @throws ApiException
     *          if the Api call fails
     */
    @Test
    public void bookmarkProjectTest() throws ApiException {
        String owner = null;
        String project = null;
        api.bookmarkProject(owner, project);

        // TODO: test validations
    }
    
    /**
     * Create new project
     *
     * 
     *
     * @throws ApiException
     *          if the Api call fails
     */
    @Test
    public void createProjectTest() throws ApiException {
        String owner = null;
        V1Project body = null;
        V1Project response = api.createProject(owner, body);

        // TODO: test validations
    }
    
    /**
     * Delete project
     *
     * 
     *
     * @throws ApiException
     *          if the Api call fails
     */
    @Test
    public void deleteProjectTest() throws ApiException {
        String owner = null;
        String project = null;
        api.deleteProject(owner, project);

        // TODO: test validations
    }
    
    /**
     * Disbale project CI
     *
     * 
     *
     * @throws ApiException
     *          if the Api call fails
     */
    @Test
    public void disableProjectCITest() throws ApiException {
        String owner = null;
        String project = null;
        api.disableProjectCI(owner, project);

        // TODO: test validations
    }
    
    /**
     * Enable project CI
     *
     * 
     *
     * @throws ApiException
     *          if the Api call fails
     */
    @Test
    public void enableProjectCITest() throws ApiException {
        String owner = null;
        String project = null;
        api.enableProjectCI(owner, project);

        // TODO: test validations
    }
    
    /**
     * Get project teams
     *
     * 
     *
     * @throws ApiException
     *          if the Api call fails
     */
    @Test
    public void fetchProjectTeamsTest() throws ApiException {
        String owner = null;
        String project = null;
        V1ProjectTeams response = api.fetchProjectTeams(owner, project);

        // TODO: test validations
    }
    
    /**
     * Get project
     *
     * 
     *
     * @throws ApiException
     *          if the Api call fails
     */
    @Test
    public void getProjectTest() throws ApiException {
        String owner = null;
        String project = null;
        V1Project response = api.getProject(owner, project);

        // TODO: test validations
    }
    
    /**
     * Get Project settings
     *
     * 
     *
     * @throws ApiException
     *          if the Api call fails
     */
    @Test
    public void getProjectSettingsTest() throws ApiException {
        String owner = null;
        String project = null;
        V1ProjectSettings response = api.getProjectSettings(owner, project);

        // TODO: test validations
    }
    
    /**
     * List archived projects for user
     *
     * 
     *
     * @throws ApiException
     *          if the Api call fails
     */
    @Test
    public void listArchivedProjectsTest() throws ApiException {
        String user = null;
        Integer offset = null;
        Integer limit = null;
        String sort = null;
        String query = null;
        V1ListProjectsResponse response = api.listArchivedProjects(user, offset, limit, sort, query);

        // TODO: test validations
    }
    
    /**
     * List bookmarked projects for user
     *
     * 
     *
     * @throws ApiException
     *          if the Api call fails
     */
    @Test
    public void listBookmarkedProjectsTest() throws ApiException {
        String user = null;
        Integer offset = null;
        Integer limit = null;
        String sort = null;
        String query = null;
        V1ListBookmarksResponse response = api.listBookmarkedProjects(user, offset, limit, sort, query);

        // TODO: test validations
    }
    
    /**
     * List project names
     *
     * 
     *
     * @throws ApiException
     *          if the Api call fails
     */
    @Test
    public void listProjectNamesTest() throws ApiException {
        String owner = null;
        Integer offset = null;
        Integer limit = null;
        String sort = null;
        String query = null;
        V1ListProjectsResponse response = api.listProjectNames(owner, offset, limit, sort, query);

        // TODO: test validations
    }
    
    /**
     * List projects
     *
     * 
     *
     * @throws ApiException
     *          if the Api call fails
     */
    @Test
    public void listProjectsTest() throws ApiException {
        String owner = null;
        Integer offset = null;
        Integer limit = null;
        String sort = null;
        String query = null;
        V1ListProjectsResponse response = api.listProjects(owner, offset, limit, sort, query);

        // TODO: test validations
    }
    
    /**
     * Patch project
     *
     * 
     *
     * @throws ApiException
     *          if the Api call fails
     */
    @Test
    public void patchProjectTest() throws ApiException {
        String owner = null;
        String projectName = null;
        V1Project body = null;
        V1Project response = api.patchProject(owner, projectName, body);

        // TODO: test validations
    }
    
    /**
     * Patch project settings
     *
     * 
     *
     * @throws ApiException
     *          if the Api call fails
     */
    @Test
    public void patchProjectSettingsTest() throws ApiException {
        String owner = null;
        String project = null;
        V1ProjectSettings body = null;
        V1ProjectSettings response = api.patchProjectSettings(owner, project, body);

        // TODO: test validations
    }
    
    /**
     * Patch project teams
     *
     * 
     *
     * @throws ApiException
     *          if the Api call fails
     */
    @Test
    public void patchProjectTeamsTest() throws ApiException {
        String owner = null;
        String project = null;
        V1ProjectTeams body = null;
        V1ProjectTeams response = api.patchProjectTeams(owner, project, body);

        // TODO: test validations
    }
    
    /**
     * Restore project
     *
     * 
     *
     * @throws ApiException
     *          if the Api call fails
     */
    @Test
    public void restoreProjectTest() throws ApiException {
        String owner = null;
        String project = null;
        api.restoreProject(owner, project);

        // TODO: test validations
    }
    
    /**
     * Unbookmark project
     *
     * 
     *
     * @throws ApiException
     *          if the Api call fails
     */
    @Test
    public void unbookmarkProjectTest() throws ApiException {
        String owner = null;
        String project = null;
        api.unbookmarkProject(owner, project);

        // TODO: test validations
    }
    
    /**
     * Update project
     *
     * 
     *
     * @throws ApiException
     *          if the Api call fails
     */
    @Test
    public void updateProjectTest() throws ApiException {
        String owner = null;
        String projectName = null;
        V1Project body = null;
        V1Project response = api.updateProject(owner, projectName, body);

        // TODO: test validations
    }
    
    /**
     * Update project settings
     *
     * 
     *
     * @throws ApiException
     *          if the Api call fails
     */
    @Test
    public void updateProjectSettingsTest() throws ApiException {
        String owner = null;
        String project = null;
        V1ProjectSettings body = null;
        V1ProjectSettings response = api.updateProjectSettings(owner, project, body);

        // TODO: test validations
    }
    
    /**
     * Update project teams
     *
     * 
     *
     * @throws ApiException
     *          if the Api call fails
     */
    @Test
    public void updateProjectTeamsTest() throws ApiException {
        String owner = null;
        String project = null;
        V1ProjectTeams body = null;
        V1ProjectTeams response = api.updateProjectTeams(owner, project, body);

        // TODO: test validations
    }
    
    /**
     * Upload artifact to a store via project access
     *
     * 
     *
     * @throws ApiException
     *          if the Api call fails
     */
    @Test
    public void uploadProjectArtifactTest() throws ApiException {
        String owner = null;
        String project = null;
        String uuid = null;
        File uploadfile = null;
        String path = null;
        Boolean overwrite = null;
        api.uploadProjectArtifact(owner, project, uuid, uploadfile, path, overwrite);

        // TODO: test validations
    }
    
}
