# automic_rest

Under construction! Not ready for use yet! Currently experimenting and planning!

## Examples of How To Use (Buggy Alpha Version)


```python
import automic_rest as automic

# init
automic.connection(
    userid='admin', 
    password='*****', 
    url='https://autmic-rest.com', 
    noproxy=True, 
    sslverify=False
)

# listExecutions 
execs = automic.executions().listExecutions(client_id=1).json()
automic.execution.executeObject()

for o in execs['data']:
    print(o['name'])

```


<table>
<thead><th>Class</th><th>Function</th><th>Infos</th></thead>
<tbody>
     <tr><td>executions</td>
     <td>changeExecutionStatus</td>
     <td>
         <ul>
             <li>summary - Changes the status of an execution.</li>
             <li>path - /{client_id}/executions/{run_id}/status</li>
             <li>method - post</li>
         </ul>
     </td></tr>
     <tr><td>executions</td>
     <td>computeErtEstimations</td>
     <td>
         <ul>
             <li>summary - Get ERT estimations for the given workflow.</li>
             <li>path - /{client_id}/executions/{run_id}/ert</li>
             <li>method - get</li>
         </ul>
     </td></tr>
     <tr><td>executions</td>
     <td>createComments</td>
     <td>
         <ul>
             <li>summary - Appends a comment to a given execution.</li>
             <li>path - /{client_id}/executions/{run_id}/comments</li>
             <li>method - post</li>
         </ul>
     </td></tr>
     <tr><td>executions</td>
     <td>executeObject</td>
     <td>
         <ul>
             <li>summary - Execute an object with or without input parameters (promptsets variables).</li>
             <li>path - /{client_id}/executions</li>
             <li>method - post</li>
         </ul>
     </td></tr>
     <tr><td>executions</td>
     <td>getChildrenOfExecution</td>
     <td>
         <ul>
             <li>summary - Gets all immediate execution children, ordered descending by activation_time and run_id.</li>
             <li>path - /{client_id}/executions/{run_id}/children</li>
             <li>method - get</li>
         </ul>
     </td></tr>
     <tr><td>executions</td>
     <td>getExecution</td>
     <td>
         <ul>
             <li>summary - Get details of a given execution.</li>
             <li>path - /{client_id}/executions/{run_id}</li>
             <li>method - get</li>
         </ul>
     </td></tr>
     <tr><td>executions</td>
     <td>listComments</td>
     <td>
         <ul>
             <li>summary - List all comments for a given execution.</li>
             <li>path - /{client_id}/executions/{run_id}/comments</li>
             <li>method - get</li>
         </ul>
     </td></tr>
     <tr><td>executions</td>
     <td>listExecutions</td>
     <td>
         <ul>
             <li>summary - List executions, ordered descending by activation_time and run_id.</li>
             <li>path - /{client_id}/executions</li>
             <li>method - get</li>
         </ul>
     </td></tr>
     <tr><td>executions</td>
     <td>listReportContent</td>
     <td>
         <ul>
             <li>summary - Report content pages.</li>
             <li>path - /{client_id}/executions/{run_id}/reports/{report_type}</li>
             <li>method - get</li>
         </ul>
     </td></tr>
     <tr><td>executions</td>
     <td>listReports</td>
     <td>
         <ul>
             <li>summary - Report list for a given execution.</li>
             <li>path - /{client_id}/executions/{run_id}/reports</li>
             <li>method - get</li>
         </ul>
     </td></tr>
     <tr><td>executions</td>
     <td>listVariables</td>
     <td>
         <ul>
             <li>summary - List all variables for a given execution.</li>
             <li>path - /{client_id}/executions/{run_id}/variables</li>
             <li>method - get</li>
         </ul>
     </td></tr>
     <tr><td>forecasts</td>
     <td>createForecast</td>
     <td>
         <ul>
             <li>summary - Create a forecast.</li>
             <li>path - /{client_id}/forecasts</li>
             <li>method - post</li>
         </ul>
     </td></tr>
     <tr><td>forecasts</td>
     <td>deleteForecast</td>
     <td>
         <ul>
             <li>summary - Delete forecasts using ids.</li>
             <li>path - /{client_id}/forecasts</li>
             <li>method - delete</li>
         </ul>
     </td></tr>
     <tr><td>forecasts</td>
     <td>getForecast</td>
     <td>
         <ul>
             <li>summary - Get details of a given forecast.</li>
             <li>path - /{client_id}/forecasts/{forecast_id}</li>
             <li>method - get</li>
         </ul>
     </td></tr>
     <tr><td>forecasts</td>
     <td>listForecastAgents</td>
     <td>
         <ul>
             <li>summary - List forecast agents and gaps.</li>
             <li>path - /{client_id}/forecasts/agents</li>
             <li>method - get</li>
         </ul>
     </td></tr>
     <tr><td>forecasts</td>
     <td>listForecasts</td>
     <td>
         <ul>
             <li>summary - List all forecasts, ordered descending by start_time.</li>
             <li>path - /{client_id}/forecasts</li>
             <li>method - get</li>
         </ul>
     </td></tr>
     <tr><td>forecasts</td>
     <td>modifyForecast</td>
     <td>
         <ul>
             <li>summary - Changes the title of a forecast item.</li>
             <li>path - /{client_id}/forecasts/{forecast_id}</li>
             <li>method - post</li>
         </ul>
     </td></tr>
     <tr><td>objects</td>
     <td>getObjects</td>
     <td>
         <ul>
             <li>summary - Can be used to export single objects by name</li>
             <li>path - /{client_id}/objects/{object_name}</li>
             <li>method - get</li>
         </ul>
     </td></tr>
     <tr><td>objects</td>
     <td>getTimezoneInfo</td>
     <td>
         <ul>
             <li>summary - Returns the time zone used by an object definition or defaults if the object or time zone does not exist.</li>       
             <li>path - /{client_id}/objects/{object_name}/timezone</li>
             <li>method - get</li>
         </ul>
     </td></tr>
     <tr><td>objects</td>
     <td>listObjectInputs</td>
     <td>
         <ul>
             <li>summary - List all inputs for a given object.</li>
             <li>path - /{client_id}/objects/{object_name}/inputs</li>
             <li>method - get</li>
         </ul>
     </td></tr>
     <tr><td>objects</td>
     <td>postObjects</td>
     <td>
         <ul>
             <li>summary - Can be used to import single objects</li>
             <li>path - /{client_id}/objects</li>
             <li>method - post</li>
         </ul>
     </td></tr>
     <tr><td>objects</td>
     <td>usage</td>
     <td>
         <ul>
             <li>summary - Returns a list of objects with a reference name, a boolean to show if the actual result has hidden objects due to acl conflicts, for the given objectname</li>
             <li>path - /{client_id}/objects/{object_name}/usage</li>
             <li>method - get</li>
         </ul>
     </td></tr>
     <tr><td>objects</td>
     <td>usageForCalendarEvents</td>
     <td>
         <ul>
             <li>summary - Returns a list of objects with a reference name, a boolean to show if the actual result has hidden objects due to acl conflicts, for the given objectname</li>
             <li>path - /{client_id}/objects/{object_name}/usage/calendarevent/{event_name}</li>
             <li>method - get</li>
         </ul>
     </td></tr>
     <tr><td>ping</td>
     <td>ping</td>
     <td>
         <ul>
             <li>summary - Can be used to determine if the JCP process is currently running.</li>
             <li>path - /ping</li>
             <li>method - get</li>
         </ul>
     </td></tr>
     <tr><td>repositories</td>
     <td>branchDiff</td>
     <td>
         <ul>
             <li>summary - Get content of two files to see their differences.</li>
             <li>path - /{client_id}/repositories/branches/{branch_name}/diff</li>
             <li>method - get</li>
         </ul>
     </td></tr>
     <tr><td>repositories</td>
     <td>branchLog</td>
     <td>
         <ul>
             <li>summary - Retrieves the history of the repository for max_results entries.</li>
             <li>path - /{client_id}/repositories/branches/{branch_name}/log</li>
             <li>method - get</li>
         </ul>
     </td></tr>
     <tr><td>repositories</td>
     <td>commitChanges</td>
     <td>
         <ul>
             <li>summary - Commits only changed objects for client to repository.</li>
             <li>path - /{client_id}/repositories/commits</li>
             <li>method - post</li>
         </ul>
     </td></tr>
     <tr><td>repositories</td>
     <td>createBranch</td>
     <td>
         <ul>
             <li>summary - Create a new branch.</li>
             <li>path - /{client_id}/repositories/branches</li>
             <li>method - post</li>
         </ul>
     </td></tr>
     <tr><td>repositories</td>
     <td>createRepository</td>
     <td>
         <ul>
             <li>summary - Initializes the repository for the specified client.</li>
             <li>path - /{client_id}/repositories</li>
             <li>method - post</li>
         </ul>
     </td></tr>
     <tr><td>repositories</td>
     <td>delete</td>
     <td>
         <ul>
             <li>summary - Abort merging so we get out of merging state.</li>
             <li>path - /{client_id}/repositories/merge</li>
             <li>method - delete</li>
         </ul>
     </td></tr>
     <tr><td>repositories</td>
     <td>getChanges</td>
     <td>
         <ul>
             <li>summary - Returns a list of objects that have uncommitted changes.</li>
             <li>path - /{client_id}/repositories/changes</li>
             <li>method - get</li>
         </ul>
     </td></tr>
     <tr><td>repositories</td>
     <td>getRepository</td>
     <td>
         <ul>
             <li>summary - Retrieves repository information for the given client.</li>
             <li>path - /{client_id}/repositories</li>
             <li>method - get</li>
         </ul>
     </td></tr>
     <tr><td>repositories</td>
     <td>listBranches</td>
     <td>
         <ul>
             <li>summary - Retrieves a list of branches.</li>
             <li>path - /{client_id}/repositories/branches</li>
             <li>method - get</li>
         </ul>
     </td></tr>
     <tr><td>repositories</td>
     <td>mergeBranchIntoActive</td>
     <td>
         <ul>
             <li>summary - Merge another branch in active branch.</li>
             <li>path - /{client_id}/repositories/merge</li>
             <li>method - post</li>
         </ul>
     </td></tr>
     <tr><td>repositories</td>
     <td>moveHead</td>
     <td>
         <ul>
             <li>summary - Imports version of provided GIT Hash to automation engine.</li>
             <li>path - /{client_id}/repositories/commits/{commit_id}</li>
             <li>method - post</li>
         </ul>
     </td></tr>
     <tr><td>repositories</td>
     <td>pull</td>
     <td>
         <ul>
             <li>summary - Pull changes from repository for active branch.</li>
             <li>path - /{client_id}/repositories/pull</li>
             <li>method - post</li>
         </ul>
     </td></tr>
     <tr><td>scripts</td>
     <td>activateScript</td>
     <td>
         <ul>
             <li>summary - Runs scripts written in the Automation Engine scripting language.</li>
             <li>path - /{client_id}/scripts</li>
             <li>method - post</li>
         </ul>
     </td></tr>
     <tr><td>search</td>
     <td>findObjects</td>
     <td>
         <ul>
             <li>summary - Search the process assembly for objects using different filter criteria.</li>
             <li>path - /{client_id}/search</li>
             <li>method - post</li>
         </ul>
     </td></tr>
     <tr><td>system</td>
     <td>deleteClients</td>
     <td>
         <ul>
             <li>summary - Delete a client</li>
             <li>path - /{client_id}/system/clients/{client_id}</li>
             <li>method - delete</li>
         </ul>
     </td></tr>
     <tr><td>system</td>
     <td>getAgentDetails</td>
     <td>
         <ul>
             <li>summary - Returns detailed agent information</li>
             <li>path - /{client_id}/system/agents/{object_name}</li>
             <li>method - get</li>
         </ul>
     </td></tr>
     <tr><td>system</td>
     <td>getFeatureList</td>
     <td>
         <ul>
             <li>summary - Retrieve system feature information.</li>
             <li>path - /{client_id}/system/features</li>
             <li>method - get</li>
         </ul>
     </td></tr>
     <tr><td>system</td>
     <td>healthCheck</td>
     <td>
         <ul>
             <li>summary - Can be used to determine if the automation system is in a healthy state. A system is healthy if there is a PWP and at least one instance of CP and JWP respectively. When healthy, HTTP 200 is returned. When unhealthy, HTTP 503. Note: only use the HTTP status code to determine the health status since the response body is optional.</li>
             <li>path - /{client_id}/system/health</li>
             <li>method - get</li>
         </ul>
     </td></tr>
     <tr><td>system</td>
     <td>listAgentgroups</td>
     <td>
         <ul>
             <li>summary - </li>
             <li>path - /{client_id}/system/agentgroups</li>
             <li>method - get</li>
         </ul>
     </td></tr>
     <tr><td>system</td>
     <td>listAgents</td>
     <td>
         <ul>
             <li>summary - Lists all agents that are defined in the system. The returned list contains running and stopped agents.</li>
             <li>path - /{client_id}/system/agents</li>
             <li>method - get</li>
         </ul>
     </td></tr>
     <tr><td>system</td>
     <td>listClients</td>
     <td>
         <ul>
             <li>summary - List of clients in the system.</li>
             <li>path - /{client_id}/system/clients</li>
             <li>method - get</li>
         </ul>
     </td></tr>
     <tr><td>telemetry</td>
     <td>export</td>
     <td>
         <ul>
             <li>summary - Retrieve telemetry data per month as json for the last n months, including the current month. Only works for client 0.</li>
             <li>path - /{client_id}/telemetry/export/{start_from}</li>
             <li>method - get</li>
         </ul>
     </td></tr>
     <tr><td>telemetry</td>
     <td>productList</td>
     <td>
         <ul>
             <li>summary - Retrieve available products</li>
             <li>path - /{client_id}/telemetry/products</li>
             <li>method - get</li>
         </ul>
     </td></tr>
</tbody>
</table>
