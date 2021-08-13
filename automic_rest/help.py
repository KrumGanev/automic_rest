class help():
    def __init__(self, module=None, html=False): 
        if module == None:
            if html:
                self.show_all_html()
            else:
                self.show_all()
        else:
            self.show_module(module)

    def show_module(self, module): 
        for parent in help_list: 
            for child in help_list[parent]:
                if child == module:
                    print("\n- " + child +"\n")
                    print("    parent  - " + parent )
                    print("    summary - " + help_list[parent][child]['summary'] )
                    print("    path    - " + help_list[parent][child]['path'] )
                    print("    method  - " + help_list[parent][child]['method'] )
                    print("")
    
    def show_all(self): 
        for parent in help_list: 
            for f in help_list[parent]: 
                print(" - " + f )
                print("     - parent  - " + parent )
                print("     - summary - " + help_list[parent][f]['summary'] )
                print("     - path    - " + help_list[parent][f]['path'] )
                print("     - method  - " + help_list[parent][f]['method'] )
                print("")
    
    def show_all_html(self): 
        import json
        
        print('## automic_rest (python client)')
        print('![version](https://img.shields.io/badge/version-0.0.5-blue) ![coverage](https://img.shields.io/badge/coverage-80%25-yellowgreen) ![state](https://img.shields.io/badge/state-dev-red) ![automic](https://img.shields.io/badge/automic-12.3-green)')
        print('#')
        print('Automic-Rest-Client generated from AE/Swagger <br>')
        print('<a >https://docs.automic.com/documentation/webhelp/english/AA/12.3/DOCU/12.3/REST%20API/Automation.Engine/swagger.json</a>')
        print('#')
        
        print("<ul>")
        for module in help_list: 
            print('     <li>')
            print('         <a href="#'+module+'">'+module+'</a>')
            print('         <ul>')
            for f in help_list[module]: 
                print('             <li><a href="#'+f+'">'+f+'</a></li>')
            print("         </ul>")
            print("     </li>")
        print("</ul>")

        for module in help_list: 
            print('     <div id="'+module+'">')
            print('     <h3>'+module+'</h3>')
            for f in help_list[module]:    
                print('         <div id="'+f+'">')
                print('         <h4>'+f+'</h4>')
                print("             <ul>")
                print("                 <li>summary - " + help_list[module][f]['summary'] + "</li>")
                print("                 <li>path - " + help_list[module][f]['path'] + "</li>")
                print("                 <li>method - " + help_list[module][f]['method'] + "</li>")
                print("             </ul>")
                print("             <div>Parameters: </div>")
                print("             <div><pre>" + json.dumps(help_list[module][f]['parameters'], indent=4, sort_keys=True) + "</pre></div>")
                print("             <div>Code-Example: </div>")
                print('             <pre>CODE</pre>')
                print('         </div>')
            print("         </ul>")
            print("     </div>")
        
        #print("<table>")
        #print("<thead><th>Class</th><th>Function</th><th>Infos</th><th>Parameters</th></thead>")
        #print("<tbody>")
        #for module in help_list: 
        #    for f in help_list[module]: 
        #        print("     <tr><td>"+module+"</td>")
        #        print("     <td>"+f+"</td>")
        #        print("     <td>")
        #        print("         <ul>")
        #        print("             <li>summary - " + help_list[module][f]['summary'] + "</li>")
        #        print("             <li>path - " + help_list[module][f]['path'] + "</li>")
        #        print("             <li>method - " + help_list[module][f]['method'] + "</li>")
        #        print("         </ul>")
        #        print("     </td>")
        #        print("     <td><pre>" + json.dumps(help_list[module][f]['parameters'], indent=4, sort_keys=True) + "</pre></td>")
        #        print("     </tr>")
        #        
        #print("</tbody>")
        #print("</table>")


help_list = {
    "executions": {
        "changeExecutionStatus": {
            "method": "post",
            "parameters": [
                {
                    "in": "body",
                    "name": "body",
                    "required": True
                }
            ],
            "path": "/{client_id}/executions/{run_id}/status",
            "summary": "Changes the status of an execution."
        },
        "computeErtEstimations": {
            "method": "get",
            "parameters": "",
            "path": "/{client_id}/executions/{run_id}/ert",
            "summary": "Get ERT estimations for the given workflow."
        },
        "createComments": {
            "method": "post",
            "parameters": [
                {
                    "in": "body",
                    "name": "body",
                    "required": True
                }
            ],
            "path": "/{client_id}/executions/{run_id}/comments",
            "summary": "Appends a comment to a given execution."
        },
        "executeObject": {
            "method": "post",
            "parameters": [
                {
                    "in": "body",
                    "name": "body",
                    "required": True
                }
            ],
            "path": "/{client_id}/executions",
            "summary": "Execute an object with or without input parameters (promptsets variables)."
        },
        "getChildrenOfExecution": {
            "method": "get",
            "parameters": [
                {
                    "description": "Maximum number of executions for a page result set. If this parameter is omitted the default value 50 is applied.",
                    "format": "int32",
                    "in": "query",
                    "minimum": 1,
                    "name": "max_results",
                    "required": False,
                    "type": "integer",
                    "x-example": 50
                },
                {
                    "description": "Requested page starts with execution with RunID > this parameter. If this parameter is omitted (no offset) the very first page is returned.",
                    "format": "int32",
                    "in": "query",
                    "name": "start_at_run_id",
                    "required": False,
                    "type": "integer",
                    "x-example": 1000030
                }
            ],
            "path": "/{client_id}/executions/{run_id}/children",
            "summary": "Gets all immediate execution children, ordered descending by activation_time and run_id."
        },
        "getExecution": {
            "method": "get",
            "parameters": [
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
                    "required": False,
                    "type": "array"
                }
            ],
            "path": "/{client_id}/executions/{run_id}",
            "summary": "Get details of a given execution."
        },
        "listComments": {
            "method": "get",
            "parameters": "",
            "path": "/{client_id}/executions/{run_id}/comments",
            "summary": "List all comments for a given execution."
        },
        "listExecutions": {
            "method": "get",
            "parameters": [
                {
                    "description": "Maximum number of executions for a page result set. If this parameter is omitted the default value 50 is applied.",
                    "format": "int32",
                    "in": "query",
                    "minimum": 1,
                    "name": "max_results",
                    "required": False,
                    "type": "integer",
                    "x-example": 50
                },
                {
                    "description": "Requested page starts with execution with RunID > this parameter. If this parameter is omitted (no offset) the very first page is returned.",
                    "format": "int32",
                    "in": "query",
                    "name": "start_at_run_id",
                    "required": False,
                    "type": "integer",
                    "x-example": 1000030
                },
                {
                    "description": "RunID of the execution.",
                    "format": "int32",
                    "in": "query",
                    "name": "run_id",
                    "required": False,
                    "type": "integer",
                    "x-example": 1000030
                },
                {
                    "description": "Object name to query. Supports wildcards (*).",
                    "in": "query",
                    "name": "name",
                    "required": False,
                    "type": "string",
                    "x-example": "SCRI.NEW.1"
                },
                {
                    "description": "Exclude object name.",
                    "in": "query",
                    "name": "name_exclude",
                    "required": False,
                    "type": "boolean",
                    "x-example": True
                },
                {
                    "description": "Object alias to query. Supports wildcards (*).",
                    "in": "query",
                    "name": "alias",
                    "required": False,
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
                    "required": False,
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
                    "required": False,
                    "type": "array",
                    "x-example": "1800"
                },
                {
                    "description": "Agent name to query. Supports wildcards (*).",
                    "in": "query",
                    "name": "agent",
                    "required": False,
                    "type": "string",
                    "x-example": "WIN01"
                },
                {
                    "description": "Exclude agent name.",
                    "in": "query",
                    "name": "agent_exclude",
                    "required": False,
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
                    "required": False,
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
                    "required": False,
                    "type": "array",
                    "x-example": "CLIENT_QUEUE"
                },
                {
                    "description": "Include deactivated executions into query.",
                    "in": "query",
                    "name": "include_deactivated",
                    "required": False,
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
                    "required": False,
                    "type": "string"
                },
                {
                    "description": "Timeframe lower bound to be used for the query.",
                    "in": "query",
                    "name": "time_frame_from",
                    "pattern": "^\\d{4}\\-(0[1-9]|1[012])\\-(0[1-9]|[12][0-9]|3[01])[T](?:[01]\\d|2[0123]):(?:[012345]\\d):(?:[012345]\\d)[Z]$",
                    "required": False,
                    "type": "string",
                    "x-example": "2015-04-15T06:37:59Z"
                },
                {
                    "description": "Timeframe upper bound to be used for the query.",
                    "in": "query",
                    "name": "time_frame_to",
                    "pattern": "^\\d{4}\\-(0[1-9]|1[012])\\-(0[1-9]|[12][0-9]|3[01])[T](?:[01]\\d|2[0123]):(?:[012345]\\d):(?:[012345]\\d)[Z]$",
                    "required": False,
                    "type": "string",
                    "x-example": "2015-04-15T06:37:59Z"
                },
                {
                    "description": "Username to query. Supports wildcards (*).",
                    "in": "query",
                    "name": "user",
                    "required": False,
                    "type": "string",
                    "x-example": "TEST/DEP"
                },
                {
                    "description": "Exclude username.",
                    "in": "query",
                    "name": "user_exclude",
                    "required": False,
                    "type": "boolean",
                    "x-example": "False"
                },
                {
                    "description": "Archive key1 to query. Supports wildcards (*).",
                    "in": "query",
                    "name": "archive_key1",
                    "required": False,
                    "type": "string",
                    "x-example": "key1"
                },
                {
                    "description": "Exclude archive key1.",
                    "in": "query",
                    "name": "archive_key1_exclude",
                    "required": False,
                    "type": "boolean",
                    "x-example": "False"
                },
                {
                    "description": "Archive key2 to query. Supports wildcards (*).",
                    "in": "query",
                    "name": "archive_key2",
                    "required": False,
                    "type": "string",
                    "x-example": "key2"
                },
                {
                    "description": "Exclude archive key2.",
                    "in": "query",
                    "name": "archive_key2_exclude",
                    "required": False,
                    "type": "boolean",
                    "x-example": "False"
                },
                {
                    "description": "Query only commented tasks.",
                    "in": "query",
                    "name": "commented_only",
                    "required": False,
                    "type": "boolean",
                    "x-example": "False"
                },
                {
                    "description": "Query only modified workflows.",
                    "in": "query",
                    "name": "modified_only",
                    "required": False,
                    "type": "boolean",
                    "x-example": "False"
                },
                {
                    "description": "Remote status text to query.",
                    "format": "int32",
                    "in": "query",
                    "name": "remote_status_number",
                    "required": False,
                    "type": "integer",
                    "x-example": 1200
                },
                {
                    "description": "Remote status number to query.",
                    "in": "query",
                    "name": "remote_status_text",
                    "required": False,
                    "type": "string",
                    "x-example": "Executed"
                },
                {
                    "description": "RunID of the original execution, zero if this was not a restart.",
                    "format": "int32",
                    "in": "query",
                    "name": "reference_run_id",
                    "required": False,
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
                    "required": False,
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
                    "required": False,
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
                    "required": False,
                    "type": "array"
                }
            ],
            "path": "/{client_id}/executions",
            "summary": "List executions, ordered descending by activation_time and run_id."
        },
        "listReportContent": {
            "method": "get",
            "parameters": [
                {
                    "description": "Type of a execution report",
                    "in": "path",
                    "name": "report_type",
                    "required": True,
                    "type": "string"
                },
                {
                    "default": 1,
                    "description": "Maximum number of report pages. If this parameter is omitted the default value 1 is applied.",
                    "format": "int32",
                    "in": "query",
                    "name": "max_results",
                    "required": False,
                    "type": "integer",
                    "x-example": 5
                },
                {
                    "default": 1,
                    "description": "Response lists report pages with numbers > this parameter.",
                    "format": "int32",
                    "in": "query",
                    "name": "start_at",
                    "required": False,
                    "type": "integer",
                    "x-example": 3
                }
            ],
            "path": "/{client_id}/executions/{run_id}/reports/{report_type}",
            "summary": "Report content pages."
        },
        "listReports": {
            "method": "get",
            "parameters": "",
            "path": "/{client_id}/executions/{run_id}/reports",
            "summary": "Report list for a given execution."
        },
        "listVariables": {
            "method": "get",
            "parameters": "",
            "path": "/{client_id}/executions/{run_id}/variables",
            "summary": "List all variables for a given execution."
        }
    },
    "forecasts": {
        "createForecast": {
            "method": "post",
            "parameters": [
                {
                    "in": "body",
                    "name": "body",
                    "required": True
                }
            ],
            "path": "/{client_id}/forecasts",
            "summary": "Create a forecast."
        },
        "deleteForecast": {
            "method": "delete",
            "parameters": [
                {
                    "in": "body",
                    "name": "body",
                    "required": False
                }
            ],
            "path": "/{client_id}/forecasts",
            "summary": "Delete forecasts using ids."
        },
        "getForecast": {
            "method": "get",
            "parameters": [
                {
                    "description": "ID of the forecast.",
                    "format": "int32",
                    "in": "path",
                    "name": "forecast_id",
                    "pattern": "\\d+",
                    "required": True,
                    "type": "integer"
                },
                {
                    "description": "Object name to query. Supports wildcards (*).",
                    "in": "query",
                    "name": "name",
                    "required": False,
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
                    "required": False,
                    "type": "array",
                    "x-example": "SCRI"
                },
                {
                    "description": "Logical start date lower bound to be used for the query.",
                    "in": "query",
                    "name": "estimated_start_from",
                    "required": False,
                    "type": "string",
                    "x-example": "2018-02-18T10:00:00Z"
                },
                {
                    "description": "Logical start date upper bound to be used for the query.",
                    "in": "query",
                    "name": "estimated_start_to",
                    "required": False,
                    "type": "string",
                    "x-example": "2018-02-19T10:00:00Z"
                },
                {
                    "description": "Agent name to query. Supports wildcards (*).",
                    "in": "query",
                    "name": "agent_destination",
                    "required": False,
                    "type": "string",
                    "x-example": "WIN01"
                },
                {
                    "description": "Source agent name to query. Supports wildcards (*).",
                    "in": "query",
                    "name": "agent_source",
                    "required": False,
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
                    "required": False,
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
                    "required": False,
                    "type": "array"
                }
            ],
            "path": "/{client_id}/forecasts/{forecast_id}",
            "summary": "Get details of a given forecast."
        },
        "listForecastAgents": {
            "method": "get",
            "parameters": [
                {
                    "description": "Agent name to query. Supports wildcards (*).",
                    "in": "query",
                    "name": "name",
                    "required": False,
                    "type": "string",
                    "x-example": "WIN01"
                },
                {
                    "description": "Agent types to query. Supports multiple, comma-separated values.",
                    "in": "query",
                    "name": "type",
                    "required": False,
                    "type": "string",
                    "x-example": "WINDOWS"
                },
                {
                    "description": "Agent version to query. Supports wildcards (*).",
                    "in": "query",
                    "name": "version",
                    "required": False,
                    "type": "string",
                    "x-example": "12.3.0+low.build.1100"
                },
                {
                    "description": "Timeframe lower bound to be used for the query.",
                    "in": "query",
                    "name": "from",
                    "required": True,
                    "type": "string",
                    "x-example": "2015-04-15T06:37:59Z"
                },
                {
                    "description": "Timeframe upper bound to be used for the query.",
                    "in": "query",
                    "name": "to",
                    "required": True,
                    "type": "string",
                    "x-example": "2015-04-15T06:37:59Z"
                },
                {
                    "description": "Timeframe upper bound to be used for the query.",
                    "in": "query",
                    "name": "execution_name",
                    "required": False,
                    "type": "string",
                    "x-example": "2015-04-15T06:37:59Z"
                },
                {
                    "description": "Minimal duration of the gap.",
                    "in": "query",
                    "name": "min_duration",
                    "pattern": "([-+]?)P(?:([-+]?[0-9]+)D)?(T(?:([-+]?[0-9]+)H)?(?:([-+]?[0-9]+)M)?(?:([-+]?[0-9]+)(?:[.,]([0-9]{0,9}))?S)?)?",
                    "required": False,
                    "type": "string",
                    "x-example": "PT9H11M34S"
                }
            ],
            "path": "/{client_id}/forecasts/agents",
            "summary": "List forecast agents and gaps."
        },
        "listForecasts": {
            "method": "get",
            "parameters": [
                {
                    "description": "Forecast title to query. Supports wildcards (*).",
                    "in": "query",
                    "name": "fc_title",
                    "required": False,
                    "type": "string",
                    "x-example": "JOBP.NEW.FORECAST"
                },
                {
                    "description": "Minimum start time to query.",
                    "in": "query",
                    "name": "fc_start_time",
                    "required": False,
                    "type": "string",
                    "x-example": "2018-02-18T10:00:00Z"
                },
                {
                    "description": "Maximum end time to query.",
                    "in": "query",
                    "name": "fc_end_time",
                    "required": False,
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
                    "required": False,
                    "type": "string",
                    "x-example": "FCST"
                },
                {
                    "description": "Object name to query. Supports wildcards (*).",
                    "in": "query",
                    "name": "name",
                    "required": False,
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
                    "required": False,
                    "type": "array",
                    "x-example": "SCRI"
                },
                {
                    "description": "Logical start date lower bound to be used for the query.",
                    "in": "query",
                    "name": "estimated_start_from",
                    "required": False,
                    "type": "string",
                    "x-example": "2018-02-18T10:00:00Z"
                },
                {
                    "description": "Logical start date upper bound to be used for the query.",
                    "in": "query",
                    "name": "estimated_start_to",
                    "required": False,
                    "type": "string",
                    "x-example": "2018-02-19T10:00:00Z"
                },
                {
                    "description": "Agent name to query. Supports wildcards (*).",
                    "in": "query",
                    "name": "agent_destination",
                    "required": False,
                    "type": "string",
                    "x-example": "WIN01"
                },
                {
                    "description": "Source agent name to query. Supports wildcards (*).",
                    "in": "query",
                    "name": "agent_source",
                    "required": False,
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
                    "required": False,
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
                    "required": False,
                    "type": "array"
                }
            ],
            "path": "/{client_id}/forecasts",
            "summary": "List all forecasts, ordered descending by start_time."
        },
        "modifyForecast": {
            "method": "post",
            "parameters": [
                {
                    "description": "ID of the forecast.",
                    "format": "int32",
                    "in": "path",
                    "name": "forecast_id",
                    "required": True,
                    "type": "integer"
                },
                {
                    "in": "body",
                    "name": "body",
                    "required": True
                }
            ],
            "path": "/{client_id}/forecasts/{forecast_id}",
            "summary": "Changes the title of a forecast item."
        }
    },
    "objects": {
        "getObjects": {
            "method": "get",
            "parameters": [
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
                    "required": False,
                    "type": "array"
                }
            ],
            "path": "/{client_id}/objects/{object_name}",
            "summary": "Can be used to export single objects by name"
        },
        "getTimezoneInfo": {
            "method": "get",
            "parameters": "",
            "path": "/{client_id}/objects/{object_name}/timezone",
            "summary": "Returns the time zone used by an object definition or defaults if the object or time zone does not exist."
        },
        "listObjectInputs": {
            "method": "get",
            "parameters": "",
            "path": "/{client_id}/objects/{object_name}/inputs",
            "summary": "List all inputs for a given object."
        },
        "postObjects": {
            "method": "post",
            "parameters": [
                {
                    "in": "body",
                    "name": "body",
                    "required": False
                },
                {
                    "default": False,
                    "description": "Determines whether existing objects should get overwritten by the import",
                    "in": "query",
                    "name": "overwrite_existing_objects",
                    "required": False,
                    "type": "boolean",
                    "x-example": True
                }
            ],
            "path": "/{client_id}/objects",
            "summary": "Can be used to import single objects"
        },
        "usageForCalendarEvents": {
            "method": "get",
            "parameters": [
                {
                    "description": "Name of the Calendar Event.",
                    "in": "path",
                    "name": "event_name",
                    "required": True,
                    "type": "string"
                }
            ],
            "path": "/{client_id}/objects/{object_name}/usage/calendarevent/{event_name}",
            "summary": "Returns a list of objects with a reference name, a boolean to show if the actual result has hidden objects due to acl conflicts, for the given objectname"
        },
        "usageObject": {
            "method": "get",
            "parameters": "",
            "path": "/{client_id}/objects/{object_name}/usage",
            "summary": "Returns a list of objects with a reference name, a boolean to show if the actual result has hidden objects due to acl conflicts, for the given objectname"
        }
    },
    "ping": {
        "ping": {
            "method": "get",
            "parameters": "",
            "path": "/ping",
            "summary": "Can be used to determine if the JCP process is currently running."
        }
    },
    "repositories": {
        "branchDiff": {
            "method": "get",
            "parameters": [
                {
                    "description": "Branch name where our file is located.",
                    "in": "path",
                    "name": "branch_name",
                    "required": True,
                    "type": "string",
                    "x-example": "master"
                },
                {
                    "description": "Branch name where their file is located.",
                    "in": "query",
                    "name": "branch_name_theirs",
                    "required": True,
                    "type": "string",
                    "x-example": "dev"
                },
                {
                    "description": "Path of the object on our branch which should be compared.",
                    "in": "query",
                    "name": "object_path_ours",
                    "required": True,
                    "type": "string",
                    "x-example": "I.AM.CONFLICTING.SCRI"
                },
                {
                    "description": "Path of the object on their branch which should be compared.",
                    "in": "query",
                    "name": "object_path_theirs",
                    "required": True,
                    "type": "string",
                    "x-example": "I.AM.CONFLICTING.SCRI"
                }
            ],
            "path": "/{client_id}/repositories/branches/{branch_name}/diff",
            "summary": "Get content of two files to see their differences."
        },
        "branchLog": {
            "method": "get",
            "parameters": [
                {
                    "description": "Name of the branch.",
                    "in": "path",
                    "name": "branch_name",
                    "required": True,
                    "type": "string"
                },
                {
                    "description": "Maximum number of executions for a page result set. If this parameter is omitted the default value 50 is applied.",
                    "format": "int32",
                    "in": "query",
                    "minimum": 1,
                    "name": "max_results",
                    "required": False,
                    "type": "integer",
                    "x-example": 50
                },
                {
                    "description": "From which history entry paging should be started.",
                    "format": "int32",
                    "in": "query",
                    "minimum": 0,
                    "name": "start_at",
                    "required": False,
                    "type": "integer"
                }
            ],
            "path": "/{client_id}/repositories/branches/{branch_name}/log",
            "summary": "Retrieves the history of the repository for max_results entries."
        },
        "commitChanges": {
            "method": "post",
            "parameters": [
                {
                    "in": "body",
                    "name": "body",
                    "required": False
                }
            ],
            "path": "/{client_id}/repositories/commits",
            "summary": "Commits only changed objects for client to repository."
        },
        "createBranch": {
            "method": "post",
            "parameters": [
                {
                    "in": "body",
                    "name": "body",
                    "required": False
                }
            ],
            "path": "/{client_id}/repositories/branches",
            "summary": "Create a new branch."
        },
        "createRepository": {
            "method": "post",
            "parameters": [
                {
                    "in": "body",
                    "name": "body",
                    "required": False
                }
            ],
            "path": "/{client_id}/repositories",
            "summary": "Initializes the repository for the specified client."
        },
        "deleteRepository": {
            "method": "delete",
            "parameters": "",
            "path": "/{client_id}/repositories/merge",
            "summary": "Abort merging so we get out of merging state."
        },
        "getChanges": {
            "method": "get",
            "parameters": [
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
                    "required": False,
                    "type": "array"
                }
            ],
            "path": "/{client_id}/repositories/changes",
            "summary": "Returns a list of objects that have uncommitted changes."
        },
        "getRepository": {
            "method": "get",
            "parameters": "",
            "path": "/{client_id}/repositories",
            "summary": "Retrieves repository information for the given client."
        },
        "listBranches": {
            "method": "get",
            "parameters": [
                {
                    "description": "Maximum number of executions for a page result set. If this parameter is omitted the default value 50 is applied.",
                    "format": "int32",
                    "in": "query",
                    "minimum": 1,
                    "name": "max_results",
                    "required": False,
                    "type": "integer",
                    "x-example": 50
                },
                {
                    "description": "From which branch list entry paging should start.",
                    "format": "int32",
                    "in": "query",
                    "minimum": 0,
                    "name": "start_at",
                    "required": False,
                    "type": "integer"
                }
            ],
            "path": "/{client_id}/repositories/branches",
            "summary": "Retrieves a list of branches."
        },
        "mergeBranchIntoActive": {
            "method": "post",
            "parameters": [
                {
                    "in": "body",
                    "name": "body",
                    "required": False
                }
            ],
            "path": "/{client_id}/repositories/merge",
            "summary": "Merge another branch in active branch."
        },
        "moveHead": {
            "method": "post",
            "parameters": [
                {
                    "description": "GIT Hash of the target commit.",
                    "in": "path",
                    "name": "commit_id",
                    "required": True,
                    "type": "string",
                    "x-example": "1"
                }
            ],
            "path": "/{client_id}/repositories/commits/{commit_id}",
            "summary": "Imports version of provided GIT Hash to automation engine."
        },
        "pullRepository": {
            "method": "post",
            "parameters": [
                {
                    "description": "Parameters for importing after a pull. The pull will abort if there are conflicts and overwriting is not enabled.",
                    "in": "body",
                    "name": "body",
                    "required": True
                }
            ],
            "path": "/{client_id}/repositories/pull",
            "summary": "Pull changes from repository for active branch."
        }
    },
    "scripts": {
        "activateScript": {
            "method": "post",
            "parameters": [
                {
                    "in": "body",
                    "name": "body",
                    "required": True
                }
            ],
            "path": "/{client_id}/scripts",
            "summary": "Runs scripts written in the Automation Engine scripting language."
        }
    },
    "search": {
        "findObjects": {
            "method": "post",
            "parameters": [
                {
                    "in": "body",
                    "name": "body",
                    "required": False
                }
            ],
            "path": "/{client_id}/search",
            "summary": "Search the process assembly for objects using different filter criteria."
        }
    },
    "system": {
        "deleteClients": {
            "method": "delete",
            "parameters": "",
            "path": "/{client_id}/system/clients/{client_id}",
            "summary": "Delete a client"
        },
        "getAgentDetails": {
            "method": "get",
            "parameters": "",
            "path": "/{client_id}/system/agents/{object_name}",
            "summary": "Returns detailed agent information"
        },
        "getFeatureList": {
            "method": "get",
            "parameters": "",
            "path": "/{client_id}/system/features",
            "summary": "Retrieve system feature information."
        },
        "healthCheck": {
            "method": "get",
            "parameters": "",
            "path": "/{client_id}/system/health",
            "summary": "Can be used to determine if the automation system is in a healthy state. A system is healthy if there is a PWP and at least one instance of CP and JWP respectively. When healthy, HTTP 200 is returned. When unhealthy, HTTP 503. Note: only use the HTTP status code to determine the health status since the response body is optional."
        },
        "listAgentgroups": {
            "method": "get",
            "parameters": "",
            "path": "/{client_id}/system/agentgroups",
            "summary": ""
        },
        "listAgents": {
            "method": "get",
            "parameters": [
                {
                    "description": "Maximum number of executions for a page result set. If this parameter is omitted the default value 50 is applied.",
                    "format": "int32",
                    "in": "query",
                    "minimum": 1,
                    "name": "max_results",
                    "required": False,
                    "type": "integer",
                    "x-example": 5000
                },
                {
                    "description": "Filter after the name of the agent. Supports wildcards (*).",
                    "in": "query",
                    "name": "name",
                    "required": False,
                    "type": "string",
                    "x-example": "WIN01"
                },
                {
                    "description": "Filter after running agents.",
                    "in": "query",
                    "name": "active",
                    "required": False,
                    "type": "boolean",
                    "x-example": True
                },
                {
                    "description": "Filter after IP address. Supports wildcards (*).",
                    "in": "query",
                    "name": "ip_address",
                    "required": False,
                    "type": "string",
                    "x-example": "10.243.20.155"
                },
                {
                    "description": "Filter after the agents version. Supports wildcards (*).",
                    "in": "query",
                    "name": "version",
                    "required": False,
                    "type": "string",
                    "x-example": "12.3.0+low.build.1100"
                },
                {
                    "description": "Filter after the computer's hardware information. Supports wildcards (*).",
                    "in": "query",
                    "name": "hardware",
                    "required": False,
                    "type": "string",
                    "x-example": "x86/2/64"
                },
                {
                    "description": "Filter after the Computer's operating system. Supports wildcards (*).",
                    "in": "query",
                    "name": "software",
                    "required": False,
                    "type": "string",
                    "x-example": "WinNT"
                },
                {
                    "description": "Filter after agents that are linked to the service manager",
                    "in": "query",
                    "name": "linked",
                    "required": False,
                    "type": "boolean",
                    "x-example": "False"
                },
                {
                    "description": "Filter after agent platform (type). Supports wildcards (*).",
                    "in": "query",
                    "name": "platform",
                    "required": False,
                    "type": "string",
                    "x-example": "WINDOWS"
                }
            ],
            "path": "/{client_id}/system/agents",
            "summary": "Lists all agents that are defined in the system. The returned list contains running and stopped agents."
        },
        "listClients": {
            "method": "get",
            "parameters": "",
            "path": "/{client_id}/system/clients",
            "summary": "List of clients in the system."
        }
    },
    "telemetry": {
        "exportTelemetry": {
            "method": "get",
            "parameters": [
                {
                    "description": "Timeframe lower bound to be used for the query.",
                    "format": "int32",
                    "in": "path",
                    "name": "start_from",
                    "required": True,
                    "type": "integer"
                }
            ],
            "path": "/{client_id}/telemetry/export/{start_from}",
            "summary": "Retrieve telemetry data per month as json for the last n months, including the current month. Only works for client 0."
        },
        "productList": {
            "method": "get",
            "parameters": "",
            "path": "/{client_id}/telemetry/products",
            "summary": "Retrieve available products"
        }
    }
}

