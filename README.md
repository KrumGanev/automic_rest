## automic_rest
![version](https://img.shields.io/badge/version-0.0.3-blue) ![coverage](https://img.shields.io/badge/coverage-80%25-yellowgreen) 
##
<ul>
     <li>
         <a href="#executions">executions</a>
         <ul>
             <li><a href="#changeExecutionStatus">changeExecutionStatus</a></li>
             <li><a href="#computeErtEstimations">computeErtEstimations</a></li>
             <li><a href="#createComments">createComments</a></li>
             <li><a href="#executeObject">executeObject</a></li>
             <li><a href="#getChildrenOfExecution">getChildrenOfExecution</a></li>
             <li><a href="#getExecution">getExecution</a></li>
             <li><a href="#listComments">listComments</a></li>
             <li><a href="#listExecutions">listExecutions</a></li>
             <li><a href="#listReportContent">listReportContent</a></li>
             <li><a href="#listReports">listReports</a></li>
             <li><a href="#listVariables">listVariables</a></li>
         </ul>
     </li>
     <li>
         <a href="#forecasts">forecasts</a>
         <ul>
             <li><a href="#createForecast">createForecast</a></li>
             <li><a href="#deleteForecast">deleteForecast</a></li>
             <li><a href="#getForecast">getForecast</a></li>
             <li><a href="#listForecastAgents">listForecastAgents</a></li>
             <li><a href="#listForecasts">listForecasts</a></li>
             <li><a href="#modifyForecast">modifyForecast</a></li>
         </ul>
     </li>
     <li>
         <a href="#objects">objects</a>
         <ul>
             <li><a href="#getObjects">getObjects</a></li>
             <li><a href="#getTimezoneInfo">getTimezoneInfo</a></li>
             <li><a href="#listObjectInputs">listObjectInputs</a></li>
             <li><a href="#postObjects">postObjects</a></li>
             <li><a href="#usageForCalendarEvents">usageForCalendarEvents</a></li>
             <li><a href="#usageObject">usageObject</a></li>
         </ul>
     </li>
     <li>
         <a href="#ping">ping</a>
         <ul>
             <li><a href="#ping">ping</a></li>
         </ul>
     </li>
     <li>
         <a href="#repositories">repositories</a>
         <ul>
             <li><a href="#branchDiff">branchDiff</a></li>
             <li><a href="#branchLog">branchLog</a></li>
             <li><a href="#commitChanges">commitChanges</a></li>
             <li><a href="#createBranch">createBranch</a></li>
             <li><a href="#createRepository">createRepository</a></li>
             <li><a href="#deleteRepository">deleteRepository</a></li>
             <li><a href="#getChanges">getChanges</a></li>
             <li><a href="#getRepository">getRepository</a></li>
             <li><a href="#listBranches">listBranches</a></li>
             <li><a href="#mergeBranchIntoActive">mergeBranchIntoActive</a></li>
             <li><a href="#moveHead">moveHead</a></li>
             <li><a href="#pullRepository">pullRepository</a></li>
         </ul>
     </li>
     <li>
         <a href="#scripts">scripts</a>
         <ul>
             <li><a href="#activateScript">activateScript</a></li>
         </ul>
     </li>
     <li>
         <a href="#search">search</a>
         <ul>
             <li><a href="#findObjects">findObjects</a></li>
         </ul>
     </li>
     <li>
         <a href="#system">system</a>
         <ul>
             <li><a href="#deleteClients">deleteClients</a></li>
             <li><a href="#getAgentDetails">getAgentDetails</a></li>
             <li><a href="#getFeatureList">getFeatureList</a></li>
             <li><a href="#healthCheck">healthCheck</a></li>
             <li><a href="#listAgentgroups">listAgentgroups</a></li>
             <li><a href="#listAgents">listAgents</a></li>
             <li><a href="#listClients">listClients</a></li>
         </ul>
     </li>
     <li>
         <a href="#telemetry">telemetry</a>
         <ul>
             <li><a href="#exportTelemetry">exportTelemetry</a></li>
             <li><a href="#productList">productList</a></li>
         </ul>
     </li>
</ul>
     <div id="executions">
     <h3>executions</h3>
         <div id="changeExecutionStatus">
         <h4>changeExecutionStatus</h4>
             <ul>
                 <li>summary - Changes the status of an execution.</li>
                 <li>path - /{client_id}/executions/{run_id}/status</li>
                 <li>method - post</li>
             </ul>
             <div>Parameters: </div>
             <div><pre>[
    {
        "in": "body",
        "name": "body",
        "required": true
    }
]</pre></div>
             <div>Code-Example: </div>
             <pre>CODE</pre>
         </div>
         <div id="computeErtEstimations">
         <h4>computeErtEstimations</h4>
             <ul>
                 <li>summary - Get ERT estimations for the given workflow.</li>
                 <li>path - /{client_id}/executions/{run_id}/ert</li>
                 <li>method - get</li>
             </ul>
             <div>Parameters: </div>
             <div><pre>""</pre></div>
             <div>Code-Example: </div>
             <pre>CODE</pre>
         </div>
         <div id="createComments">
         <h4>createComments</h4>
             <ul>
                 <li>summary - Appends a comment to a given execution.</li>
                 <li>path - /{client_id}/executions/{run_id}/comments</li>
                 <li>method - post</li>
             </ul>
             <div>Parameters: </div>
             <div><pre>[
    {
        "in": "body",
        "name": "body",
        "required": true
    }
]</pre></div>
             <div>Code-Example: </div>
             <pre>CODE</pre>
         </div>
         <div id="executeObject">
         <h4>executeObject</h4>
             <ul>
                 <li>summary - Execute an object with or without input parameters (promptsets variables).</li>
                 <li>path - /{client_id}/executions</li>
                 <li>method - post</li>
             </ul>
             <div>Parameters: </div>
             <div><pre>[
    {
        "in": "body",
        "name": "body",
        "required": true
    }
]</pre></div>
             <div>Code-Example: </div>
             <pre>CODE</pre>
         </div>
         <div id="getChildrenOfExecution">
         <h4>getChildrenOfExecution</h4>
             <ul>
                 <li>summary - Gets all immediate execution children, ordered descending by activation_time and run_id.</li>
                 <li>path - /{client_id}/executions/{run_id}/children</li>
                 <li>method - get</li>
             </ul>
             <div>Parameters: </div>
             <div><pre>[
    {
        "description": "Maximum number of executions for a page result set. If this parameter is omitted the default value 50 is applied.",
        "format": "int32",
        "in": "query",
        "minimum": 1,
        "name": "max_results",
        "required": false,
        "type": "integer",
        "x-example": 50
    },
    {
        "description": "Requested page starts with execution with RunID > this parameter. If this parameter is omitted (no offset) the very first page is returned.",
        "format": "int32",
        "in": "query",
        "name": "start_at_run_id",
        "required": false,
        "type": "integer",
        "x-example": 1000030
    }
]</pre></div>
             <div>Code-Example: </div>
             <pre>CODE</pre>
         </div>
         <div id="getExecution">
         <h4>getExecution</h4>
             <ul>
                 <li>summary - Get details of a given execution.</li>
                 <li>path - /{client_id}/executions/{run_id}</li>
                 <li>method - get</li>
             </ul>
             <div>Parameters: </div>
             <div><pre>[
    {
        "collectionFormat": "multi",
        "description": "Parameter to include various additional information about an execution.<br><strong>comments</strong> - Includes a list of all comments that have been added to the execution<br><strong>variables</strong> - Includes a list of all object variables defined at the execution's scope<br><strong>reports</strong> - Includes a list of all report types of the execution<br><strong>restarts</strong> - Includes the number of restarts<br><strong>predecessors</strong> - Includes a list of the predecessors of a workflow task<br><strong>recurring</strong> - Includes details of a C_PERIOD task",
        "in": "query",
        "items": {
            "enum": [
                "comments",
                "variables",
                "reports",
                "restarts",
                "predecessors",
                "recurring"
            ],
            "type": "string"
        },
        "name": "fields",
        "required": false,
        "type": "array"
    }
]</pre></div>
             <div>Code-Example: </div>
             <pre>CODE</pre>
         </div>
         <div id="listComments">
         <h4>listComments</h4>
             <ul>
                 <li>summary - List all comments for a given execution.</li>
                 <li>path - /{client_id}/executions/{run_id}/comments</li>
                 <li>method - get</li>
             </ul>
             <div>Parameters: </div>
             <div><pre>""</pre></div>
             <div>Code-Example: </div>
             <pre>CODE</pre>
         </div>
         <div id="listExecutions">
         <h4>listExecutions</h4>
             <ul>
                 <li>summary - List executions, ordered descending by activation_time and run_id.</li>
                 <li>path - /{client_id}/executions</li>
                 <li>method - get</li>
             </ul>
             <div>Parameters: </div>
             <div><pre>[
    {
        "description": "Maximum number of executions for a page result set. If this parameter is omitted the default value 50 is applied.",
        "format": "int32",
        "in": "query",
        "minimum": 1,
        "name": "max_results",
        "required": false,
        "type": "integer",
        "x-example": 50
    },
    {
        "description": "Requested page starts with execution with RunID > this parameter. If this parameter is omitted (no offset) the very first page is returned.",
        "format": "int32",
        "in": "query",
        "name": "start_at_run_id",
        "required": false,
        "type": "integer",
        "x-example": 1000030
    },
    {
        "description": "RunID of the execution.",
        "format": "int32",
        "in": "query",
        "name": "run_id",
        "required": false,
        "type": "integer",
        "x-example": 1000030
    },
    {
        "description": "Object name to query. Supports wildcards (*).",
        "in": "query",
        "name": "name",
        "required": false,
        "type": "string",
        "x-example": "SCRI.NEW.1"
    },
    {
        "description": "Exclude object name.",
        "in": "query",
        "name": "name_exclude",
        "required": false,
        "type": "boolean",
        "x-example": true
    },
    {
        "description": "Object alias to query. Supports wildcards (*).",
        "in": "query",
        "name": "alias",
        "required": false,
        "type": "string",
        "x-example": "SCRI.ALIAS.1"
    },
    {
        "collectionFormat": "multi",
        "description": "Object types to query. Supports multiple, comma-separated values. If omitted, all executable object types are used as default value.",
        "in": "query",
        "items": {
            "type": "string"
        },
        "name": "type",
        "required": false,
        "type": "array",
        "x-example": "SCRI"
    },
    {
        "collectionFormat": "multi",
        "description": "Status to query. Supports multiple, comma-separated values.",
        "in": "query",
        "items": {
            "type": "string"
        },
        "name": "status",
        "required": false,
        "type": "array",
        "x-example": "1800"
    },
    {
        "description": "Agent name to query. Supports wildcards (*).",
        "in": "query",
        "name": "agent",
        "required": false,
        "type": "string",
        "x-example": "WIN01"
    },
    {
        "description": "Exclude agent name.",
        "in": "query",
        "name": "agent_exclude",
        "required": false,
        "type": "boolean",
        "x-example": "False"
    },
    {
        "collectionFormat": "multi",
        "description": "Agent types to query. Supports multiple, comma-separated values.",
        "in": "query",
        "items": {
            "type": "string"
        },
        "name": "platform",
        "required": false,
        "type": "array",
        "x-example": "WINDOWS"
    },
    {
        "collectionFormat": "multi",
        "description": "Queues to query. Supports multiple, comma-separated values.",
        "in": "query",
        "items": {
            "type": "string"
        },
        "name": "queue",
        "required": false,
        "type": "array",
        "x-example": "CLIENT_QUEUE"
    },
    {
        "description": "Include deactivated executions into query.",
        "in": "query",
        "name": "include_deactivated",
        "required": false,
        "type": "boolean",
        "x-example": "False"
    },
    {
        "description": "Timeframe option to be used for the query. If omitted, the default value of 'all' is applied.",
        "enum": [
            "activation",
            "start",
            "end",
            "all"
        ],
        "in": "query",
        "name": "time_frame_option",
        "required": false,
        "type": "string"
    },
    {
        "description": "Timeframe lower bound to be used for the query.",
        "in": "query",
        "name": "time_frame_from",
        "pattern": "^\\d{4}\\-(0[1-9]|1[012])\\-(0[1-9]|[12][0-9]|3[01])[T](?:[01]\\d|2[0123]):(?:[012345]\\d):(?:[012345]\\d)[Z]$",
        "required": false,
        "type": "string",
        "x-example": "2015-04-15T06:37:59Z"
    },
    {
        "description": "Timeframe upper bound to be used for the query.",
        "in": "query",
        "name": "time_frame_to",
        "pattern": "^\\d{4}\\-(0[1-9]|1[012])\\-(0[1-9]|[12][0-9]|3[01])[T](?:[01]\\d|2[0123]):(?:[012345]\\d):(?:[012345]\\d)[Z]$",
        "required": false,
        "type": "string",
        "x-example": "2015-04-15T06:37:59Z"
    },
    {
        "description": "Username to query. Supports wildcards (*).",
        "in": "query",
        "name": "user",
        "required": false,
        "type": "string",
        "x-example": "TEST/DEP"
    },
    {
        "description": "Exclude username.",
        "in": "query",
        "name": "user_exclude",
        "required": false,
        "type": "boolean",
        "x-example": "False"
    },
    {
        "description": "Archive key1 to query. Supports wildcards (*).",
        "in": "query",
        "name": "archive_key1",
        "required": false,
        "type": "string",
        "x-example": "key1"
    },
    {
        "description": "Exclude archive key1.",
        "in": "query",
        "name": "archive_key1_exclude",
        "required": false,
        "type": "boolean",
        "x-example": "False"
    },
    {
        "description": "Archive key2 to query. Supports wildcards (*).",
        "in": "query",
        "name": "archive_key2",
        "required": false,
        "type": "string",
        "x-example": "key2"
    },
    {
        "description": "Exclude archive key2.",
        "in": "query",
        "name": "archive_key2_exclude",
        "required": false,
        "type": "boolean",
        "x-example": "False"
    },
    {
        "description": "Query only commented tasks.",
        "in": "query",
        "name": "commented_only",
        "required": false,
        "type": "boolean",
        "x-example": "False"
    },
    {
        "description": "Query only modified workflows.",
        "in": "query",
        "name": "modified_only",
        "required": false,
        "type": "boolean",
        "x-example": "False"
    },
    {
        "description": "Remote status text to query.",
        "format": "int32",
        "in": "query",
        "name": "remote_status_number",
        "required": false,
        "type": "integer",
        "x-example": 1200
    },
    {
        "description": "Remote status number to query.",
        "in": "query",
        "name": "remote_status_text",
        "required": false,
        "type": "string",
        "x-example": "Executed"
    },
    {
        "description": "RunID of the original execution, zero if this was not a restart.",
        "format": "int32",
        "in": "query",
        "name": "reference_run_id",
        "required": false,
        "type": "integer",
        "x-example": 1000031
    },
    {
        "description": "Query ZDU Version.",
        "enum": [
            "B",
            "T"
        ],
        "in": "query",
        "name": "zdu_version",
        "pattern": "([BT])",
        "required": false,
        "type": "string"
    },
    {
        "collectionFormat": "multi",
        "description": "Sync objects to query. Supports multiple, comma-separated values.",
        "in": "query",
        "items": {
            "type": "string"
        },
        "name": "sync_usage",
        "required": false,
        "type": "array",
        "x-example": "SYNC1"
    },
    {
        "collectionFormat": "multi",
        "description": "Parameter to include various additional information about an execution.<br><strong>restarts</strong> - Includes the number of restarts<br><strong>predecessors</strong> - Includes a list of the predecessors of a workflow task<strong>recurring</strong> - Includes details of a C_PERIOD task",
        "in": "query",
        "items": {
            "enum": [
                "restarts",
                "predecessors",
                "recurring"
            ],
            "type": "string"
        },
        "name": "fields",
        "required": false,
        "type": "array"
    }
]</pre></div>
             <div>Code-Example: </div>
             <pre>CODE</pre>
         </div>
         <div id="listReportContent">
         <h4>listReportContent</h4>
             <ul>
                 <li>summary - Report content pages.</li>
                 <li>path - /{client_id}/executions/{run_id}/reports/{report_type}</li>
                 <li>method - get</li>
             </ul>
             <div>Parameters: </div>
             <div><pre>[
    {
        "description": "Type of a execution report",
        "in": "path",
        "name": "report_type",
        "required": true,
        "type": "string"
    },
    {
        "default": 1,
        "description": "Maximum number of report pages. If this parameter is omitted the default value 1 is applied.",
        "format": "int32",
        "in": "query",
        "name": "max_results",
        "required": false,
        "type": "integer",
        "x-example": 5
    },
    {
        "default": 1,
        "description": "Response lists report pages with numbers > this parameter.",
        "format": "int32",
        "in": "query",
        "name": "start_at",
        "required": false,
        "type": "integer",
        "x-example": 3
    }
]</pre></div>
             <div>Code-Example: </div>
             <pre>CODE</pre>
         </div>
         <div id="listReports">
         <h4>listReports</h4>
             <ul>
                 <li>summary - Report list for a given execution.</li>
                 <li>path - /{client_id}/executions/{run_id}/reports</li>
                 <li>method - get</li>
             </ul>
             <div>Parameters: </div>
             <div><pre>""</pre></div>
             <div>Code-Example: </div>
             <pre>CODE</pre>
         </div>
         <div id="listVariables">
         <h4>listVariables</h4>
             <ul>
                 <li>summary - List all variables for a given execution.</li>
                 <li>path - /{client_id}/executions/{run_id}/variables</li>
                 <li>method - get</li>
             </ul>
             <div>Parameters: </div>
             <div><pre>""</pre></div>
             <div>Code-Example: </div>
             <pre>CODE</pre>
         </div>
         </ul>
     </div>
     <div id="forecasts">
     <h3>forecasts</h3>
         <div id="createForecast">
         <h4>createForecast</h4>
             <ul>
                 <li>summary - Create a forecast.</li>
                 <li>path - /{client_id}/forecasts</li>
                 <li>method - post</li>
             </ul>
             <div>Parameters: </div>
             <div><pre>[
    {
        "in": "body",
        "name": "body",
        "required": true
    }
]</pre></div>
             <div>Code-Example: </div>
             <pre>CODE</pre>
         </div>
         <div id="deleteForecast">
         <h4>deleteForecast</h4>
             <ul>
                 <li>summary - Delete forecasts using ids.</li>
                 <li>path - /{client_id}/forecasts</li>
                 <li>method - delete</li>
             </ul>
             <div>Parameters: </div>
             <div><pre>[
    {
        "in": "body",
        "name": "body",
        "required": false
    }
]</pre></div>
             <div>Code-Example: </div>
             <pre>CODE</pre>
         </div>
         <div id="getForecast">
         <h4>getForecast</h4>
             <ul>
                 <li>summary - Get details of a given forecast.</li>
                 <li>path - /{client_id}/forecasts/{forecast_id}</li>
                 <li>method - get</li>
             </ul>
             <div>Parameters: </div>
             <div><pre>[
    {
        "description": "ID of the forecast.",
        "format": "int32",
        "in": "path",
        "name": "forecast_id",
        "pattern": "\\d+",
        "required": true,
        "type": "integer"
    },
    {
        "description": "Object name to query. Supports wildcards (*).",
        "in": "query",
        "name": "name",
        "required": false,
        "type": "string",
        "x-example": "SCRI.NEW.1"
    },
    {
        "collectionFormat": "multi",
        "description": "Object types to query. Supports multiple, comma-separated values. If omitted, all executable object types are used as default value.",
        "in": "query",
        "items": {
            "type": "string"
        },
        "name": "type",
        "required": false,
        "type": "array",
        "x-example": "SCRI"
    },
    {
        "description": "Logical start date lower bound to be used for the query.",
        "in": "query",
        "name": "estimated_start_from",
        "required": false,
        "type": "string",
        "x-example": "2018-02-18T10:00:00Z"
    },
    {
        "description": "Logical start date upper bound to be used for the query.",
        "in": "query",
        "name": "estimated_start_to",
        "required": false,
        "type": "string",
        "x-example": "2018-02-19T10:00:00Z"
    },
    {
        "description": "Agent name to query. Supports wildcards (*).",
        "in": "query",
        "name": "agent_destination",
        "required": false,
        "type": "string",
        "x-example": "WIN01"
    },
    {
        "description": "Source agent name to query. Supports wildcards (*).",
        "in": "query",
        "name": "agent_source",
        "required": false,
        "type": "string",
        "x-example": "WIN01"
    },
    {
        "collectionFormat": "multi",
        "description": "Agent platform to query. Supports multiple, comma-separated values.",
        "in": "query",
        "items": {
            "type": "string"
        },
        "name": "platform_destination",
        "required": false,
        "type": "array",
        "x-example": "WINDOWS"
    },
    {
        "collectionFormat": "multi",
        "description": "Parameter to include various additional information about a forecast.<br><strong>entries</strong> - Includes a list of all entries within a forecast",
        "in": "query",
        "items": {
            "enum": [
                "entries"
            ],
            "type": "string"
        },
        "name": "fields",
        "required": false,
        "type": "array"
    }
]</pre></div>
             <div>Code-Example: </div>
             <pre>CODE</pre>
         </div>
         <div id="listForecastAgents">
         <h4>listForecastAgents</h4>
             <ul>
                 <li>summary - List forecast agents and gaps.</li>
                 <li>path - /{client_id}/forecasts/agents</li>
                 <li>method - get</li>
             </ul>
             <div>Parameters: </div>
             <div><pre>[
    {
        "description": "Agent name to query. Supports wildcards (*).",
        "in": "query",
        "name": "name",
        "required": false,
        "type": "string",
        "x-example": "WIN01"
    },
    {
        "description": "Agent types to query. Supports multiple, comma-separated values.",
        "in": "query",
        "name": "type",
        "required": false,
        "type": "string",
        "x-example": "WINDOWS"
    },
    {
        "description": "Agent version to query. Supports wildcards (*).",
        "in": "query",
        "name": "version",
        "required": false,
        "type": "string",
        "x-example": "12.3.0+low.build.1100"
    },
    {
        "description": "Timeframe lower bound to be used for the query.",
        "in": "query",
        "name": "from",
        "required": true,
        "type": "string",
        "x-example": "2015-04-15T06:37:59Z"
    },
    {
        "description": "Timeframe upper bound to be used for the query.",
        "in": "query",
        "name": "to",
        "required": true,
        "type": "string",
        "x-example": "2015-04-15T06:37:59Z"
    },
    {
        "description": "Timeframe upper bound to be used for the query.",
        "in": "query",
        "name": "execution_name",
        "required": false,
        "type": "string",
        "x-example": "2015-04-15T06:37:59Z"
    },
    {
        "description": "Minimal duration of the gap.",
        "in": "query",
        "name": "min_duration",
        "pattern": "([-+]?)P(?:([-+]?[0-9]+)D)?(T(?:([-+]?[0-9]+)H)?(?:([-+]?[0-9]+)M)?(?:([-+]?[0-9]+)(?:[.,]([0-9]{0,9}))?S)?)?",
        "required": false,
        "type": "string",
        "x-example": "PT9H11M34S"
    }
]</pre></div>
             <div>Code-Example: </div>
             <pre>CODE</pre>
         </div>
         <div id="listForecasts">
         <h4>listForecasts</h4>
             <ul>
                 <li>summary - List all forecasts, ordered descending by start_time.</li>
                 <li>path - /{client_id}/forecasts</li>
                 <li>method - get</li>
             </ul>
             <div>Parameters: </div>
             <div><pre>[
    {
        "description": "Forecast title to query. Supports wildcards (*).",
        "in": "query",
        "name": "fc_title",
        "required": false,
        "type": "string",
        "x-example": "JOBP.NEW.FORECAST"
    },
    {
        "description": "Minimum start time to query.",
        "in": "query",
        "name": "fc_start_time",
        "required": false,
        "type": "string",
        "x-example": "2018-02-18T10:00:00Z"
    },
    {
        "description": "Maximum end time to query.",
        "in": "query",
        "name": "fc_end_time",
        "required": false,
        "type": "string",
        "x-example": "2018-02-19T10:00:00Z"
    },
    {
        "description": "Forecast type to query. Omit to get all types.",
        "enum": [
            "FCST",
            "AFCST"
        ],
        "in": "query",
        "name": "fc_type",
        "required": false,
        "type": "string",
        "x-example": "FCST"
    },
    {
        "description": "Object name to query. Supports wildcards (*).",
        "in": "query",
        "name": "name",
        "required": false,
        "type": "string",
        "x-example": "SCRI.NEW.1"
    },
    {
        "collectionFormat": "multi",
        "description": "Object types to query. Supports multiple, comma-separated values. If omitted, all executable object types are used as default value.",
        "in": "query",
        "items": {
            "type": "string"
        },
        "name": "type",
        "required": false,
        "type": "array",
        "x-example": "SCRI"
    },
    {
        "description": "Logical start date lower bound to be used for the query.",
        "in": "query",
        "name": "estimated_start_from",
        "required": false,
        "type": "string",
        "x-example": "2018-02-18T10:00:00Z"
    },
    {
        "description": "Logical start date upper bound to be used for the query.",
        "in": "query",
        "name": "estimated_start_to",
        "required": false,
        "type": "string",
        "x-example": "2018-02-19T10:00:00Z"
    },
    {
        "description": "Agent name to query. Supports wildcards (*).",
        "in": "query",
        "name": "agent_destination",
        "required": false,
        "type": "string",
        "x-example": "WIN01"
    },
    {
        "description": "Source agent name to query. Supports wildcards (*).",
        "in": "query",
        "name": "agent_source",
        "required": false,
        "type": "string",
        "x-example": "WIN01"
    },
    {
        "collectionFormat": "multi",
        "description": "Agent platform to query. Supports multiple, comma-separated values.",
        "in": "query",
        "items": {
            "type": "string"
        },
        "name": "platform_destination",
        "required": false,
        "type": "array",
        "x-example": "WINDOWS"
    },
    {
        "collectionFormat": "multi",
        "description": "Parameter to include various additional information about a forecast.<br><strong>entries</strong> - Includes a list of all entries within a forecast",
        "in": "query",
        "items": {
            "enum": [
                "entries"
            ],
            "type": "string"
        },
        "name": "fields",
        "required": false,
        "type": "array"
    }
]</pre></div>
             <div>Code-Example: </div>
             <pre>CODE</pre>
         </div>
         <div id="modifyForecast">
         <h4>modifyForecast</h4>
             <ul>
                 <li>summary - Changes the title of a forecast item.</li>
                 <li>path - /{client_id}/forecasts/{forecast_id}</li>
                 <li>method - post</li>
             </ul>
             <div>Parameters: </div>
             <div><pre>[
    {
        "description": "ID of the forecast.",
        "format": "int32",
        "in": "path",
        "name": "forecast_id",
        "required": true,
        "type": "integer"
    },
    {
        "in": "body",
        "name": "body",
        "required": true
    }
]</pre></div>
             <div>Code-Example: </div>
             <pre>CODE</pre>
         </div>
         </ul>
     </div>
     <div id="objects">
     <h3>objects</h3>
         <div id="getObjects">
         <h4>getObjects</h4>
             <ul>
                 <li>summary - Can be used to export single objects by name</li>
                 <li>path - /{client_id}/objects/{object_name}</li>
                 <li>method - get</li>
             </ul>
             <div>Parameters: </div>
             <div><pre>[
    {
        "collectionFormat": "multi",
        "description": "Optional list of additional fields.<br><strong>modification_details</strong> - Includes modification/creation date and user name.<br>",
        "in": "query",
        "items": {
            "enum": [
                "modification_details"
            ],
            "type": "string"
        },
        "name": "fields",
        "required": false,
        "type": "array"
    }
]</pre></div>
             <div>Code-Example: </div>
             <pre>CODE</pre>
         </div>
         <div id="getTimezoneInfo">
         <h4>getTimezoneInfo</h4>
             <ul>
                 <li>summary - Returns the time zone used by an object definition or defaults if the object or time zone does not exist.</li>
                 <li>path - /{client_id}/objects/{object_name}/timezone</li>
                 <li>method - get</li>
             </ul>
             <div>Parameters: </div>
             <div><pre>""</pre></div>
             <div>Code-Example: </div>
             <pre>CODE</pre>
         </div>
         <div id="listObjectInputs">
         <h4>listObjectInputs</h4>
             <ul>
                 <li>summary - List all inputs for a given object.</li>
                 <li>path - /{client_id}/objects/{object_name}/inputs</li>
                 <li>method - get</li>
             </ul>
             <div>Parameters: </div>
             <div><pre>""</pre></div>
             <div>Code-Example: </div>
             <pre>CODE</pre>
         </div>
         <div id="postObjects">
         <h4>postObjects</h4>
             <ul>
                 <li>summary - Can be used to import single objects</li>
                 <li>path - /{client_id}/objects</li>
                 <li>method - post</li>
             </ul>
             <div>Parameters: </div>
             <div><pre>[
    {
        "in": "body",
        "name": "body",
        "required": false
    },
    {
        "default": false,
        "description": "Determines whether existing objects should get overwritten by the import",
        "in": "query",
        "name": "overwrite_existing_objects",
        "required": false,
        "type": "boolean",
        "x-example": true
    }
]</pre></div>
             <div>Code-Example: </div>
             <pre>CODE</pre>
         </div>
         <div id="usageForCalendarEvents">
         <h4>usageForCalendarEvents</h4>
             <ul>
                 <li>summary - Returns a list of objects with a reference name, a boolean to show if the actual result has hidden objects due to acl conflicts, for the given objectname</li>
                 <li>path - /{client_id}/objects/{object_name}/usage/calendarevent/{event_name}</li>
                 <li>method - get</li>
             </ul>
             <div>Parameters: </div>
             <div><pre>[
    {
        "description": "Name of the Calendar Event.",
        "in": "path",
        "name": "event_name",
        "required": true,
        "type": "string"
    }
]</pre></div>
             <div>Code-Example: </div>
             <pre>CODE</pre>
         </div>
         <div id="usageObject">
         <h4>usageObject</h4>
             <ul>
                 <li>summary - Returns a list of objects with a reference name, a boolean to show if the actual result has hidden objects due to acl conflicts, for the given objectname</li>
                 <li>path - /{client_id}/objects/{object_name}/usage</li>
                 <li>method - get</li>
             </ul>
             <div>Parameters: </div>
             <div><pre>""</pre></div>
             <div>Code-Example: </div>
             <pre>CODE</pre>
         </div>
         </ul>
     </div>
     <div id="ping">
     <h3>ping</h3>
         <div id="ping">
         <h4>ping</h4>
             <ul>
                 <li>summary - Can be used to determine if the JCP process is currently running.</li>
                 <li>path - /ping</li>
                 <li>method - get</li>
             </ul>
             <div>Parameters: </div>
             <div><pre>""</pre></div>
             <div>Code-Example: </div>
             <pre>CODE</pre>
         </div>
         </ul>
     </div>
     <div id="repositories">
     <h3>repositories</h3>
         <div id="branchDiff">
         <h4>branchDiff</h4>
             <ul>
                 <li>summary - Get content of two files to see their differences.</li>
                 <li>path - /{client_id}/repositories/branches/{branch_name}/diff</li>
                 <li>method - get</li>
             </ul>
             <div>Parameters: </div>
             <div><pre>[
    {
        "description": "Branch name where our file is located.",
        "in": "path",
        "name": "branch_name",
        "required": true,
        "type": "string",
        "x-example": "master"
    },
    {
        "description": "Branch name where their file is located.",
        "in": "query",
        "name": "branch_name_theirs",
        "required": true,
        "type": "string",
        "x-example": "dev"
    },
    {
        "description": "Path of the object on our branch which should be compared.",
        "in": "query",
        "name": "object_path_ours",
        "required": true,
        "type": "string",
        "x-example": "I.AM.CONFLICTING.SCRI"
    },
    {
        "description": "Path of the object on their branch which should be compared.",
        "in": "query",
        "name": "object_path_theirs",
        "required": true,
        "type": "string",
        "x-example": "I.AM.CONFLICTING.SCRI"
    }
]</pre></div>
             <div>Code-Example: </div>
             <pre>CODE</pre>
         </div>
         <div id="branchLog">
         <h4>branchLog</h4>
             <ul>
                 <li>summary - Retrieves the history of the repository for max_results entries.</li>
                 <li>path - /{client_id}/repositories/branches/{branch_name}/log</li>
                 <li>method - get</li>
             </ul>
             <div>Parameters: </div>
             <div><pre>[
    {
        "description": "Name of the branch.",
        "in": "path",
        "name": "branch_name",
        "required": true,
        "type": "string"
    },
    {
        "description": "Maximum number of executions for a page result set. If this parameter is omitted the default value 50 is applied.",
        "format": "int32",
        "in": "query",
        "minimum": 1,
        "name": "max_results",
        "required": false,
        "type": "integer",
        "x-example": 50
    },
    {
        "description": "From which history entry paging should be started.",
        "format": "int32",
        "in": "query",
        "minimum": 0,
        "name": "start_at",
        "required": false,
        "type": "integer"
    }
]</pre></div>
             <div>Code-Example: </div>
             <pre>CODE</pre>
         </div>
         <div id="commitChanges">
         <h4>commitChanges</h4>
             <ul>
                 <li>summary - Commits only changed objects for client to repository.</li>
                 <li>path - /{client_id}/repositories/commits</li>
                 <li>method - post</li>
             </ul>
             <div>Parameters: </div>
             <div><pre>[
    {
        "in": "body",
        "name": "body",
        "required": false
    }
]</pre></div>
             <div>Code-Example: </div>
             <pre>CODE</pre>
         </div>
         <div id="createBranch">
         <h4>createBranch</h4>
             <ul>
                 <li>summary - Create a new branch.</li>
                 <li>path - /{client_id}/repositories/branches</li>
                 <li>method - post</li>
             </ul>
             <div>Parameters: </div>
             <div><pre>[
    {
        "in": "body",
        "name": "body",
        "required": false
    }
]</pre></div>
             <div>Code-Example: </div>
             <pre>CODE</pre>
         </div>
         <div id="createRepository">
         <h4>createRepository</h4>
             <ul>
                 <li>summary - Initializes the repository for the specified client.</li>
                 <li>path - /{client_id}/repositories</li>
                 <li>method - post</li>
             </ul>
             <div>Parameters: </div>
             <div><pre>[
    {
        "in": "body",
        "name": "body",
        "required": false
    }
]</pre></div>
             <div>Code-Example: </div>
             <pre>CODE</pre>
         </div>
         <div id="deleteRepository">
         <h4>deleteRepository</h4>
             <ul>
                 <li>summary - Abort merging so we get out of merging state.</li>
                 <li>path - /{client_id}/repositories/merge</li>
                 <li>method - delete</li>
             </ul>
             <div>Parameters: </div>
             <div><pre>""</pre></div>
             <div>Code-Example: </div>
             <pre>CODE</pre>
         </div>
         <div id="getChanges">
         <h4>getChanges</h4>
             <ul>
                 <li>summary - Returns a list of objects that have uncommitted changes.</li>
                 <li>path - /{client_id}/repositories/changes</li>
                 <li>method - get</li>
             </ul>
             <div>Parameters: </div>
             <div><pre>[
    {
        "collectionFormat": "multi",
        "description": "Parameter to include various additional information about changes.<br><strong>total</strong> - the total number of uncommitted files.<br>",
        "in": "query",
        "items": {
            "enum": [
                "total"
            ],
            "type": "string"
        },
        "name": "fields",
        "required": false,
        "type": "array"
    }
]</pre></div>
             <div>Code-Example: </div>
             <pre>CODE</pre>
         </div>
         <div id="getRepository">
         <h4>getRepository</h4>
             <ul>
                 <li>summary - Retrieves repository information for the given client.</li>
                 <li>path - /{client_id}/repositories</li>
                 <li>method - get</li>
             </ul>
             <div>Parameters: </div>
             <div><pre>""</pre></div>
             <div>Code-Example: </div>
             <pre>CODE</pre>
         </div>
         <div id="listBranches">
         <h4>listBranches</h4>
             <ul>
                 <li>summary - Retrieves a list of branches.</li>
                 <li>path - /{client_id}/repositories/branches</li>
                 <li>method - get</li>
             </ul>
             <div>Parameters: </div>
             <div><pre>[
    {
        "description": "Maximum number of executions for a page result set. If this parameter is omitted the default value 50 is applied.",
        "format": "int32",
        "in": "query",
        "minimum": 1,
        "name": "max_results",
        "required": false,
        "type": "integer",
        "x-example": 50
    },
    {
        "description": "From which branch list entry paging should start.",
        "format": "int32",
        "in": "query",
        "minimum": 0,
        "name": "start_at",
        "required": false,
        "type": "integer"
    }
]</pre></div>
             <div>Code-Example: </div>
             <pre>CODE</pre>
         </div>
         <div id="mergeBranchIntoActive">
         <h4>mergeBranchIntoActive</h4>
             <ul>
                 <li>summary - Merge another branch in active branch.</li>
                 <li>path - /{client_id}/repositories/merge</li>
                 <li>method - post</li>
             </ul>
             <div>Parameters: </div>
             <div><pre>[
    {
        "in": "body",
        "name": "body",
        "required": false
    }
]</pre></div>
             <div>Code-Example: </div>
             <pre>CODE</pre>
         </div>
         <div id="moveHead">
         <h4>moveHead</h4>
             <ul>
                 <li>summary - Imports version of provided GIT Hash to automation engine.</li>
                 <li>path - /{client_id}/repositories/commits/{commit_id}</li>
                 <li>method - post</li>
             </ul>
             <div>Parameters: </div>
             <div><pre>[
    {
        "description": "GIT Hash of the target commit.",
        "in": "path",
        "name": "commit_id",
        "required": true,
        "type": "string",
        "x-example": "1"
    }
]</pre></div>
             <div>Code-Example: </div>
             <pre>CODE</pre>
         </div>
         <div id="pullRepository">
         <h4>pullRepository</h4>
             <ul>
                 <li>summary - Pull changes from repository for active branch.</li>
                 <li>path - /{client_id}/repositories/pull</li>
                 <li>method - post</li>
             </ul>
             <div>Parameters: </div>
             <div><pre>[
    {
        "description": "Parameters for importing after a pull. The pull will abort if there are conflicts and overwriting is not enabled.",
        "in": "body",
        "name": "body",
        "required": true
    }
]</pre></div>
             <div>Code-Example: </div>
             <pre>CODE</pre>
         </div>
         </ul>
     </div>
     <div id="scripts">
     <h3>scripts</h3>
         <div id="activateScript">
         <h4>activateScript</h4>
             <ul>
                 <li>summary - Runs scripts written in the Automation Engine scripting language.</li>
                 <li>path - /{client_id}/scripts</li>
                 <li>method - post</li>
             </ul>
             <div>Parameters: </div>
             <div><pre>[
    {
        "in": "body",
        "name": "body",
        "required": true
    }
]</pre></div>
             <div>Code-Example: </div>
             <pre>CODE</pre>
         </div>
         </ul>
     </div>
     <div id="search">
     <h3>search</h3>
         <div id="findObjects">
         <h4>findObjects</h4>
             <ul>
                 <li>summary - Search the process assembly for objects using different filter criteria.</li>
                 <li>path - /{client_id}/search</li>
                 <li>method - post</li>
             </ul>
             <div>Parameters: </div>
             <div><pre>[
    {
        "in": "body",
        "name": "body",
        "required": false
    }
]</pre></div>
             <div>Code-Example: </div>
             <pre>CODE</pre>
         </div>
         </ul>
     </div>
     <div id="system">
     <h3>system</h3>
         <div id="deleteClients">
         <h4>deleteClients</h4>
             <ul>
                 <li>summary - Delete a client</li>
                 <li>path - /{client_id}/system/clients/{client_id}</li>
                 <li>method - delete</li>
             </ul>
             <div>Parameters: </div>
             <div><pre>""</pre></div>
             <div>Code-Example: </div>
             <pre>CODE</pre>
         </div>
         <div id="getAgentDetails">
         <h4>getAgentDetails</h4>
             <ul>
                 <li>summary - Returns detailed agent information</li>
                 <li>path - /{client_id}/system/agents/{object_name}</li>
                 <li>method - get</li>
             </ul>
             <div>Parameters: </div>
             <div><pre>""</pre></div>
             <div>Code-Example: </div>
             <pre>CODE</pre>
         </div>
         <div id="getFeatureList">
         <h4>getFeatureList</h4>
             <ul>
                 <li>summary - Retrieve system feature information.</li>
                 <li>path - /{client_id}/system/features</li>
                 <li>method - get</li>
             </ul>
             <div>Parameters: </div>
             <div><pre>""</pre></div>
             <div>Code-Example: </div>
             <pre>CODE</pre>
         </div>
         <div id="healthCheck">
         <h4>healthCheck</h4>
             <ul>
                 <li>summary - Can be used to determine if the automation system is in a healthy state. A system is healthy if there is a PWP and at least one instance of CP and JWP respectively. When healthy, HTTP 200 is returned. When unhealthy, HTTP 503. Note: only use the HTTP status code to determine the health status since the response body is optional.</li>
                 <li>path - /{client_id}/system/health</li>
                 <li>method - get</li>
             </ul>
             <div>Parameters: </div>
             <div><pre>""</pre></div>
             <div>Code-Example: </div>
             <pre>CODE</pre>
         </div>
         <div id="listAgentgroups">
         <h4>listAgentgroups</h4>
             <ul>
                 <li>summary - </li>
                 <li>path - /{client_id}/system/agentgroups</li>
                 <li>method - get</li>
             </ul>
             <div>Parameters: </div>
             <div><pre>""</pre></div>
             <div>Code-Example: </div>
             <pre>CODE</pre>
         </div>
         <div id="listAgents">
         <h4>listAgents</h4>
             <ul>
                 <li>summary - Lists all agents that are defined in the system. The returned list contains running and stopped agents.</li>
                 <li>path - /{client_id}/system/agents</li>
                 <li>method - get</li>
             </ul>
             <div>Parameters: </div>
             <div><pre>[
    {
        "description": "Maximum number of executions for a page result set. If this parameter is omitted the default value 50 is applied.",
        "format": "int32",
        "in": "query",
        "minimum": 1,
        "name": "max_results",
        "required": false,
        "type": "integer",
        "x-example": 5000
    },
    {
        "description": "Filter after the name of the agent. Supports wildcards (*).",
        "in": "query",
        "name": "name",
        "required": false,
        "type": "string",
        "x-example": "WIN01"
    },
    {
        "description": "Filter after running agents.",
        "in": "query",
        "name": "active",
        "required": false,
        "type": "boolean",
        "x-example": true
    },
    {
        "description": "Filter after IP address. Supports wildcards (*).",
        "in": "query",
        "name": "ip_address",
        "required": false,
        "type": "string",
        "x-example": "10.243.20.155"
    },
    {
        "description": "Filter after the agents version. Supports wildcards (*).",
        "in": "query",
        "name": "version",
        "required": false,
        "type": "string",
        "x-example": "12.3.0+low.build.1100"
    },
    {
        "description": "Filter after the computer's hardware information. Supports wildcards (*).",
        "in": "query",
        "name": "hardware",
        "required": false,
        "type": "string",
        "x-example": "x86/2/64"
    },
    {
        "description": "Filter after the Computer's operating system. Supports wildcards (*).",
        "in": "query",
        "name": "software",
        "required": false,
        "type": "string",
        "x-example": "WinNT"
    },
    {
        "description": "Filter after agents that are linked to the service manager",
        "in": "query",
        "name": "linked",
        "required": false,
        "type": "boolean",
        "x-example": "False"
    },
    {
        "description": "Filter after agent platform (type). Supports wildcards (*).",
        "in": "query",
        "name": "platform",
        "required": false,
        "type": "string",
        "x-example": "WINDOWS"
    }
]</pre></div>
             <div>Code-Example: </div>
             <pre>CODE</pre>
         </div>
         <div id="listClients">
         <h4>listClients</h4>
             <ul>
                 <li>summary - List of clients in the system.</li>
                 <li>path - /{client_id}/system/clients</li>
                 <li>method - get</li>
             </ul>
             <div>Parameters: </div>
             <div><pre>""</pre></div>
             <div>Code-Example: </div>
             <pre>CODE</pre>
         </div>
         </ul>
     </div>
     <div id="telemetry">
     <h3>telemetry</h3>
         <div id="exportTelemetry">
         <h4>exportTelemetry</h4>
             <ul>
                 <li>summary - Retrieve telemetry data per month as json for the last n months, including the current month. Only works for client 0.</li>
                 <li>path - /{client_id}/telemetry/export/{start_from}</li>
                 <li>method - get</li>
             </ul>
             <div>Parameters: </div>
             <div><pre>[
    {
        "description": "Timeframe lower bound to be used for the query.",
        "format": "int32",
        "in": "path",
        "name": "start_from",
        "required": true,
        "type": "integer"
    }
]</pre></div>
             <div>Code-Example: </div>
             <pre>CODE</pre>
         </div>
         <div id="productList">
         <h4>productList</h4>
             <ul>
                 <li>summary - Retrieve available products</li>
                 <li>path - /{client_id}/telemetry/products</li>
                 <li>method - get</li>
             </ul>
             <div>Parameters: </div>
             <div><pre>""</pre></div>
             <div>Code-Example: </div>
             <pre>CODE</pre>
         </div>
         </ul>
     </div>
