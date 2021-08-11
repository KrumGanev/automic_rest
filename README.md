*   executions
   *   changeExecutionStatus
      *   summary - Changes the status of an execution.
      *   path - /{client_id}/executions/{run_id}/status
      *   method - post

   *   computeErtEstimations
      *   summary - Get ERT estimations for the given workflow.
      *   path - /{client_id}/executions/{run_id}/ert
      *   method - get

   *   createComments
      *   summary - Appends a comment to a given execution.
      *   path - /{client_id}/executions/{run_id}/comments
      *   method - post

   *   executeObject
      *   summary - Execute an object with or without input parameters (promptsets variables).
      *   path - /{client_id}/executions
      *   method - post

   *   getChildrenOfExecution
      *   summary - Gets all immediate execution children, ordered descending by activation_time and run_id.
      *   path - /{client_id}/executions/{run_id}/children
      *   method - get

   *   getExecution
      *   summary - Get details of a given execution.
      *   path - /{client_id}/executions/{run_id}
      *   method - get

   *   listComments
      *   summary - List all comments for a given execution.
      *   path - /{client_id}/executions/{run_id}/comments
      *   method - get

   *   listExecutions
      *   summary - List executions, ordered descending by activation_time and run_id.
      *   path - /{client_id}/executions
      *   method - get

   *   listReportContent
      *   summary - Report content pages.
      *   path - /{client_id}/executions/{run_id}/reports/{report_type}
      *   method - get

   *   listReports
      *   summary - Report list for a given execution.
      *   path - /{client_id}/executions/{run_id}/reports
      *   method - get

   *   listVariables
      *   summary - List all variables for a given execution.
      *   path - /{client_id}/executions/{run_id}/variables
      *   method - get

*   forecasts
   *   createForecast
      *   summary - Create a forecast.
      *   path - /{client_id}/forecasts
      *   method - post

   *   deleteForecast
      *   summary - Delete forecasts using ids.
      *   path - /{client_id}/forecasts
      *   method - delete

   *   getForecast
      *   summary - Get details of a given forecast.
      *   path - /{client_id}/forecasts/{forecast_id}
      *   method - get

   *   listForecastAgents
      *   summary - List forecast agents and gaps.
      *   path - /{client_id}/forecasts/agents
      *   method - get

   *   listForecasts
      *   summary - List all forecasts, ordered descending by start_time.
      *   path - /{client_id}/forecasts
      *   method - get

   *   modifyForecast
      *   summary - Changes the title of a forecast item.
      *   path - /{client_id}/forecasts/{forecast_id}
      *   method - post

*   objects
   *   getObjects
      *   summary - Can be used to export single objects by name
      *   path - /{client_id}/objects/{object_name}
      *   method - get

   *   getTimezoneInfo
      *   summary - Returns the time zone used by an object definition or defaults if the object or time zone does not exist.
      *   path - /{client_id}/objects/{object_name}/timezone
      *   method - get

   *   listObjectInputs
      *   summary - List all inputs for a given object.
      *   path - /{client_id}/objects/{object_name}/inputs
      *   method - get

   *   postObjects
      *   summary - Can be used to import single objects
      *   path - /{client_id}/objects
      *   method - post

   *   usage
      *   summary - Returns a list of objects with a reference name, a boolean to show if the actual result has hidden objects due to acl conflicts, for the given objectname
      *   path - /{client_id}/objects/{object_name}/usage
      *   method - get

   *   usageForCalendarEvents
      *   summary - Returns a list of objects with a reference name, a boolean to show if the actual result has hidden objects due to acl conflicts, for the given objectname
      *   path - /{client_id}/objects/{object_name}/usage/calendarevent/{event_name}
      *   method - get

*   ping
   *   ping
      *   summary - Can be used to determine if the JCP process is currently running.
      *   path - /ping
      *   method - get

*   repositories
   *   branchDiff
      *   summary - Get content of two files to see their differences.
      *   path - /{client_id}/repositories/branches/{branch_name}/diff
      *   method - get

   *   branchLog
      *   summary - Retrieves the history of the repository for max_results entries.
      *   path - /{client_id}/repositories/branches/{branch_name}/log
      *   method - get

   *   commitChanges
      *   summary - Commits only changed objects for client to repository.
      *   path - /{client_id}/repositories/commits
      *   method - post

   *   createBranch
      *   summary - Create a new branch.
      *   path - /{client_id}/repositories/branches
      *   method - post

   *   createRepository
      *   summary - Initializes the repository for the specified client.
      *   path - /{client_id}/repositories
      *   method - post

   *   delete
      *   summary - Abort merging so we get out of merging state.
      *   path - /{client_id}/repositories/merge
      *   method - delete

   *   getChanges
      *   summary - Returns a list of objects that have uncommitted changes.
      *   path - /{client_id}/repositories/changes
      *   method - get

   *   getRepository
      *   summary - Retrieves repository information for the given client.
      *   path - /{client_id}/repositories
      *   method - get

   *   listBranches
      *   summary - Retrieves a list of branches.
      *   path - /{client_id}/repositories/branches
      *   method - get

   *   mergeBranchIntoActive
      *   summary - Merge another branch in active branch.
      *   path - /{client_id}/repositories/merge
      *   method - post

   *   moveHead
      *   summary - Imports version of provided GIT Hash to automation engine.
      *   path - /{client_id}/repositories/commits/{commit_id}
      *   method - post

   *   pull
      *   summary - Pull changes from repository for active branch.
      *   path - /{client_id}/repositories/pull
      *   method - post

*   scripts
   *   activateScript
      *   summary - Runs scripts written in the Automation Engine scripting language.
      *   path - /{client_id}/scripts
      *   method - post

*   search
   *   findObjects
      *   summary - Search the process assembly for objects using different filter criteria.
      *   path - /{client_id}/search
      *   method - post

*   system
   *   deleteClients
      *   summary - Delete a client
      *   path - /{client_id}/system/clients/{client_id}
      *   method - delete

   *   getAgentDetails
      *   summary - Returns detailed agent information
      *   path - /{client_id}/system/agents/{object_name}
      *   method - get

   *   getFeatureList
      *   summary - Retrieve system feature information.
      *   path - /{client_id}/system/features
      *   method - get

   *   healthCheck
      *   summary - Can be used to determine if the automation system is in a healthy state. A system is healthy if there is a PWP and at least 
one instance of CP and JWP respectively. When healthy, HTTP 200 is returned. When unhealthy, HTTP 503. Note: only use the HTTP status code to determine the health status since the response body is optional.
      *   path - /{client_id}/system/health
      *   method - get

   *   listAgentgroups
      *   summary -
      *   path - /{client_id}/system/agentgroups
      *   method - get

   *   listAgents
      *   summary - Lists all agents that are defined in the system. The returned list contains running and stopped agents.
      *   path - /{client_id}/system/agents
      *   method - get

   *   listClients
      *   summary - List of clients in the system.
      *   path - /{client_id}/system/clients
      *   method - get

*   telemetry
   *   export
      *   summary - Retrieve telemetry data per month as json for the last n months, including the current month. Only works for client 0.      
      *   path - /{client_id}/telemetry/export/{start_from}
      *   method - get

   *   productList
      *   summary - Retrieve available products
      *   path - /{client_id}/telemetry/products
      *   method - get
