Search.setIndex({docnames:["cli","core","exporters","index","intro","modules","server"],envversion:{"sphinx.domains.c":2,"sphinx.domains.changeset":1,"sphinx.domains.citation":1,"sphinx.domains.cpp":2,"sphinx.domains.index":1,"sphinx.domains.javascript":2,"sphinx.domains.math":2,"sphinx.domains.python":2,"sphinx.domains.rst":2,"sphinx.domains.std":1,"sphinx.ext.intersphinx":1,"sphinx.ext.todo":2,"sphinx.ext.viewcode":1,sphinx:56},filenames:["cli.rst","core.rst","exporters.rst","index.rst","intro.rst","modules.rst","server.rst"],objects:{"":{cli:[0,0,0,"-"]},"hidebound.core":{config:[1,0,0,"-"],database:[1,0,0,"-"],database_tools:[1,0,0,"-"],parser:[1,0,0,"-"],specification_base:[1,0,0,"-"],specifications:[1,0,0,"-"],tools:[1,0,0,"-"],traits:[1,0,0,"-"],validators:[1,0,0,"-"]},"hidebound.core.config":{Config:[1,3,1,""],is_hidebound_directory:[1,2,1,""],is_specification_file:[1,2,1,""]},"hidebound.core.config.Config":{ExportersConfig:[1,3,1,""],_schema:[1,4,1,""],exclude_regex:[1,4,1,"id0"],exporters:[1,4,1,"id1"],hidebound_directory:[1,4,1,"id2"],include_regex:[1,4,1,"id3"],root_directory:[1,4,1,"id4"],specification_files:[1,4,1,"id5"],write_mode:[1,4,1,"id6"]},"hidebound.core.config.Config.ExportersConfig":{_schema:[1,4,1,""],girder:[1,4,1,""]},"hidebound.core.database":{Database:[1,3,1,""]},"hidebound.core.database.Database":{"delete":[1,5,1,""],"export":[1,5,1,""],create:[1,5,1,""],from_config:[1,5,1,""],from_json:[1,5,1,""],read:[1,5,1,""],search:[1,5,1,""],update:[1,5,1,""]},"hidebound.core.database_tools":{_add_asset_id:[1,2,1,""],_add_asset_name:[1,2,1,""],_add_asset_path:[1,2,1,""],_add_asset_traits:[1,2,1,""],_add_asset_type:[1,2,1,""],_add_file_traits:[1,2,1,""],_add_relative_path:[1,2,1,""],_add_specification:[1,2,1,""],_cleanup:[1,2,1,""],_get_data_for_write:[1,2,1,""],_validate_assets:[1,2,1,""],_validate_filepath:[1,2,1,""]},"hidebound.core.parser":{AssetNameParser:[1,3,1,""]},"hidebound.core.parser.AssetNameParser":{COORDINATE_INDICATOR:[1,4,1,""],COORDINATE_PADDING:[1,4,1,""],DESCRIPTOR_INDICATOR:[1,4,1,""],EXTENSION_INDICATOR:[1,4,1,""],FIELD_SEPARATOR:[1,4,1,""],FRAME_INDICATOR:[1,4,1,""],FRAME_PADDING:[1,4,1,""],LEGAL_FIELDS:[1,4,1,""],PROJECT_INDICATOR:[1,4,1,""],SPECIFICATION_INDICATOR:[1,4,1,""],TOKEN_SEPARATOR:[1,4,1,""],VERSION_INDICATOR:[1,4,1,""],VERSION_PADDING:[1,4,1,""],_get_extension_parser:[1,5,1,""],_get_grammar:[1,5,1,""],_get_parser:[1,5,1,""],_get_specification_parser:[1,5,1,""],_raise_field_error:[1,5,1,""],parse:[1,5,1,""],parse_specification:[1,5,1,""],to_string:[1,5,1,""]},"hidebound.core.specification_base":{ComplexSpecificationBase:[1,3,1,""],FileSpecificationBase:[1,3,1,""],SequenceSpecificationBase:[1,3,1,""],SpecificationBase:[1,3,1,""]},"hidebound.core.specification_base.ComplexSpecificationBase":{_schema:[1,4,1,""],asset_type:[1,4,1,"id7"],descriptor:[1,4,1,""],extension:[1,4,1,""],project:[1,4,1,""],specification:[1,4,1,""],version:[1,4,1,""]},"hidebound.core.specification_base.FileSpecificationBase":{_schema:[1,4,1,""],asset_type:[1,4,1,"id8"],descriptor:[1,4,1,""],extension:[1,4,1,""],get_asset_path:[1,5,1,""],project:[1,4,1,""],specification:[1,4,1,""],version:[1,4,1,""]},"hidebound.core.specification_base.SequenceSpecificationBase":{_schema:[1,4,1,""],asset_type:[1,4,1,"id9"],descriptor:[1,4,1,""],extension:[1,4,1,""],get_asset_path:[1,5,1,""],project:[1,4,1,""],specification:[1,4,1,""],version:[1,4,1,""]},"hidebound.core.specification_base.SpecificationBase":{_schema:[1,4,1,""],asset_name_fields:[1,4,1,"id10"],asset_type:[1,4,1,"id11"],descriptor:[1,4,1,"id12"],extension:[1,4,1,"id13"],file_traits:[1,4,1,""],filename_fields:[1,4,1,"id14"],get_asset_id:[1,5,1,""],get_asset_name:[1,5,1,""],get_asset_path:[1,5,1,""],get_file_traits:[1,5,1,""],get_filename_traits:[1,5,1,""],get_traits:[1,5,1,""],project:[1,4,1,"id15"],specification:[1,4,1,""],validate_filepath:[1,5,1,""],version:[1,4,1,"id16"]},"hidebound.core.specifications":{Raw001:[1,3,1,""],Raw002:[1,3,1,""]},"hidebound.core.specifications.Raw001":{_schema:[1,4,1,""],asset_name_fields:[1,4,1,"id17"],channels:[1,4,1,""],descriptor:[1,4,1,""],extension:[1,4,1,"id18"],file_traits:[1,4,1,""],filename_fields:[1,4,1,"id19"],frame:[1,4,1,""],height:[1,4,1,"id20"],project:[1,4,1,""],specification:[1,4,1,""],version:[1,4,1,""],width:[1,4,1,"id21"]},"hidebound.core.specifications.Raw002":{_schema:[1,4,1,""],asset_name_fields:[1,4,1,"id22"],channels:[1,4,1,""],coordinate:[1,4,1,""],descriptor:[1,4,1,""],extension:[1,4,1,"id23"],file_traits:[1,4,1,""],filename_fields:[1,4,1,"id24"],frame:[1,4,1,""],height:[1,4,1,"id25"],project:[1,4,1,""],specification:[1,4,1,""],version:[1,4,1,""],width:[1,4,1,"id26"]},"hidebound.core.tools":{StopWatch:[1,3,1,""],directory_to_dataframe:[1,2,1,""],error_to_string:[1,2,1,""],list_all_files:[1,2,1,""],relative_path:[1,2,1,""],to_prototype:[1,2,1,""],try_:[1,2,1,""]},"hidebound.core.tools.StopWatch":{delta:[1,5,1,""],human_readable_delta:[1,5,1,""],start:[1,5,1,""],stop:[1,5,1,""]},"hidebound.core.traits":{get_image_channels:[1,2,1,""],get_image_height:[1,2,1,""],get_image_width:[1,2,1,""]},"hidebound.core.validators":{is_attribute_of:[1,2,1,""],is_coordinate:[1,2,1,""],is_descriptor:[1,2,1,""],is_directory:[1,2,1,""],is_eq:[1,2,1,""],is_extension:[1,2,1,""],is_file:[1,2,1,""],is_frame:[1,2,1,""],is_gt:[1,2,1,""],is_homogenous:[1,2,1,""],is_in:[1,2,1,""],is_lt:[1,2,1,""],is_project:[1,2,1,""],is_version:[1,2,1,""],validate:[1,2,1,""],validate_each:[1,2,1,""]},"hidebound.exporters":{exporter_base:[2,0,0,"-"],girder_exporter:[2,0,0,"-"]},"hidebound.exporters.exporter_base":{ExporterBase:[2,3,1,""]},"hidebound.exporters.exporter_base.ExporterBase":{"export":[2,5,1,""],_enforce_directory_structure:[2,5,1,""],_export_asset:[2,5,1,""],_export_file:[2,5,1,""]},"hidebound.exporters.girder_exporter":{GirderConfig:[2,3,1,""],GirderExporter:[2,3,1,""]},"hidebound.exporters.girder_exporter.GirderConfig":{_schema:[2,4,1,""],api_key:[2,4,1,"id0"],host:[2,4,1,"id1"],port:[2,4,1,"id2"],root_id:[2,4,1,"id3"],root_type:[2,4,1,"id4"]},"hidebound.exporters.girder_exporter.GirderExporter":{_export_asset:[2,5,1,""],_export_dirs:[2,5,1,""],_export_file:[2,5,1,""],from_config:[2,5,1,""]},"hidebound.server":{api:[6,0,0,"-"],app:[6,0,0,"-"],components:[6,0,0,"-"],server_tools:[6,0,0,"-"]},"hidebound.server.api":{"delete":[6,2,1,""],"export":[6,2,1,""],api:[6,2,1,""],create:[6,2,1,""],handle_data_error:[6,2,1,""],initialize:[6,2,1,""],read:[6,2,1,""],search:[6,2,1,""],update:[6,2,1,""]},"hidebound.server.app":{on_config_card_update:[6,2,1,""],on_datatable_update:[6,2,1,""],on_event:[6,2,1,""],on_get_tab:[6,2,1,""],serve_stylesheet:[6,2,1,""]},"hidebound.server.components":{get_asset_graph:[6,2,1,""],get_button:[6,2,1,""],get_config_tab:[6,2,1,""],get_configbar:[6,2,1,""],get_dash_app:[6,2,1,""],get_data_tab:[6,2,1,""],get_datatable:[6,2,1,""],get_dropdown:[6,2,1,""],get_dummy_elements:[6,2,1,""],get_key_value_card:[6,2,1,""],get_searchbar:[6,2,1,""]},"hidebound.server.server_tools":{error_to_response:[6,2,1,""],get_config_error:[6,2,1,""],get_initialization_error:[6,2,1,""],get_read_error:[6,2,1,""],get_search_error:[6,2,1,""],get_update_error:[6,2,1,""],parse_json_file_content:[6,2,1,""],render_template:[6,2,1,""],setup_hidebound_directory:[6,2,1,""]},cli:{REPO_PATH:[0,1,1,""],get_app_command:[0,2,1,""],get_architecture_diagram_command:[0,2,1,""],get_bash_command:[0,2,1,""],get_container_id_command:[0,2,1,""],get_coverage_command:[0,2,1,""],get_destroy_production_container_command:[0,2,1,""],get_docker_command:[0,2,1,""],get_docker_compose_command:[0,2,1,""],get_docker_exec_command:[0,2,1,""],get_docs_command:[0,2,1,""],get_fix_permissions_command:[0,2,1,""],get_image_id_command:[0,2,1,""],get_info:[0,2,1,""],get_lab_command:[0,2,1,""],get_lint_command:[0,2,1,""],get_package_command:[0,2,1,""],get_production_container_command:[0,2,1,""],get_production_image_command:[0,2,1,""],get_publish_command:[0,2,1,""],get_python_command:[0,2,1,""],get_radon_metrics_command:[0,2,1,""],get_remove_image_command:[0,2,1,""],get_remove_pycache_command:[0,2,1,""],get_requirements_command:[0,2,1,""],get_start_command:[0,2,1,""],get_stop_command:[0,2,1,""],get_test_command:[0,2,1,""],get_tox_command:[0,2,1,""],get_type_checking_command:[0,2,1,""],main:[0,2,1,""]}},objnames:{"0":["py","module","Python module"],"1":["py","data","Python data"],"2":["py","function","Python function"],"3":["py","class","Python class"],"4":["py","attribute","Python attribute"],"5":["py","method","Python method"]},objtypes:{"0":"py:module","1":"py:data","2":"py:function","3":"py:class","4":"py:attribute","5":"py:method"},terms:{"0005_f0001":4,"0005_f0002":4,"0005_f0003":4,"005_f0001":4,"005_f0002":4,"005_f0003":4,"279873a2":4,"40b3":4,"4eb1":4,"7dc4f771f992":4,"871h":[],"891723hdsasd":[],"976f":[],"abstract":2,"boolean":1,"byte":6,"case":4,"catch":1,"class":[1,2,4],"default":[0,1,2,6],"export":[1,3,5,6],"final":[2,4],"function":[1,4,6],"import":1,"int":[1,2,6],"new":4,"return":[0,1,2,6],"static":[1,2],"throw":6,"true":[0,1,2],AWS:4,For:[1,3],Its:4,One:6,That:4,The:[1,4],These:4,Use:4,Using:4,______:[],_______:4,__dict__:[],__doc__:[],__file__:1,__init__:[],__module__:[],__name__:[],__weakref__:[],_add_asset_id:1,_add_asset_nam:1,_add_asset_path:1,_add_asset_trait:1,_add_asset_typ:1,_add_file_trait:1,_add_filename_data:[],_add_filename_trait:[],_add_relative_path:1,_add_specif:1,_cleanup:1,_enforce_directory_structur:2,_export_asset:2,_export_dir:2,_export_fil:2,_get_data_for_writ:1,_get_extension_pars:1,_get_grammar:1,_get_ordered_pars:[],_get_pars:1,_get_specification_pars:1,_get_unordered_pars:[],_id:2,_raise_field_error:1,_schema:[1,2],_validate_asset:1,_validate_filepath:1,a6bc3b756cc5:4,a9f3727c:4,abf2:4,abov:4,accord:[1,4],accur:[],acronynm:4,add:1,added:1,adding:4,address:2,aforement:4,after:1,again:4,age:0,aggreg:1,agnost:0,akjsd879:[],all:[0,1,2,3,4,6],alloc:4,alreadi:2,alskhdu12632:[],also:4,alwai:[1,4],amazon:4,ani:[1,2,4,6],api:[2,3,5],api_kei:2,app:[0,3,4,5],app_data:[1,2],append:2,appli:1,applic:3,appropri:4,arbitrari:[1,4],arbitrarili:4,arg:0,argument:1,asgdhjhg:[],askl:[],asset:[1,2,3,6],asset_directori:[],asset_error:1,asset_id:1,asset_metadata:1,asset_nam:1,asset_name_field:1,asset_path:[1,6],asset_path_rel:2,asset_trait:1,asset_typ:[1,2],asset_valid:[1,6],assetnamepars:1,associ:4,assosci:[],assum:6,attempt:1,attribut:[1,4],b4a2:[],b766:4,back:4,backward:4,bar:[],base:[1,2,4],bash:0,bc84:4,been:[1,2],befor:1,begin:4,behind:4,below:4,beyond:[],bfd0:4,bin:4,block:1,bool:[1,2],broken:4,build:0,built:0,button:[4,6],c001:4,calico:4,call:[1,4],callabl:1,callback:6,can:[1,4],capit:4,captur:1,card:6,cat001:4,cat001_:4,cat:4,cat_v001:4,cat_v001_c000:4,cb8f:4,cb9b:4,cell:1,chang:4,channel:[1,4],charact:4,check:0,child:6,chmod:4,choos:4,chown:0,chunk:4,clean:1,cli:[3,5],click:4,client:[2,6],clone:4,code:[0,1,3,4],collaps:4,collect:2,color:4,column:[1,4,6],columnn:[],com:4,command:[0,4],compat:4,competitor:4,complet:4,complex:[1,3,4],complexspecificationbas:1,compon:[3,5],compos:[0,4],compris:4,concept:4,concern:4,config:[2,3,5,6],config_path:6,configur:[1,2,4,6],conform:4,conig:4,consid:[],consist:[1,4],constitu:4,construct:[1,2,4],consumpt:4,contain:[0,1,2,4],content:[1,4,6],continu:[],conveni:[1,4,6],convent:3,convert:[1,4],coordin:[1,4],coordinate_ind:1,coordinate_pad:1,copi:[1,4],core:[3,5,6],correct:[1,4],could:[1,4],coverag:[0,3],creat:[0,1,3,6],create_button:[],crude:4,current:[0,1,4],custom:1,cyan:4,cyclomat:3,cytoscap:6,dash:6,dash_core_compon:6,dash_cytoscap:6,dash_html_compon:6,dash_tabl:6,dashaceeditor:[],data:[1,2,3,6],databas:[3,4,5,6],database_tool:[3,5],dataerror:[1,2,6],datafram:1,datat:6,debug:[],debug_mod:[],decor:1,deepli:0,defin:[1,4],delet:[1,3,6],delete_button:[],delta:1,depend:[0,1,4],deploi:0,deprec:[1,2],deriv:[1,4],descriptor:[1,4],descriptor_ind:1,deserialize_map:[1,2],design:4,destroi:0,detail:[0,4],determin:4,detrmin:[],develop:[0,3],diagnos:3,diagram:3,dict:[0,1,2,6],dict_:1,dictionari:[0,1,2,6],differ:[0,4],directli:1,directori:[0,1,2,4,6],directory_to_datafram:1,dirpath:2,dirtectori:2,discov:4,displai:[4,6],distinct:4,div:6,divid:4,doc:[0,3],docker:[0,2,3],document:[0,4,6],doe:[1,4,6],doubt:4,down:0,drawn:4,dropdown:[4,6],ds_store:1,dump:4,duplic:[],dynimc:1,e06ab7e64bd9:[],e50160a:4,ea95bd79:4,each:[1,4,6],easili:1,edit:[],editor:6,ee8311b1f0c9:4,efe734c5f65c:4,either:4,element:[4,6],ellips:4,empti:[],enabl:4,encapsul:4,encount:1,encourag:3,end:4,ensur:[1,2,4],entireti:4,entiti:2,env_var:0,environ:0,equal:[1,4],error:[1,3,6],error_to_respons:6,error_to_str:1,especi:4,etc:4,evalu:4,everi:4,everyth:4,exactli:4,exampl:[1,3],except:[1,4,6],exclud:1,exclude_regex:1,exec:0,exist:[1,2,4,6],exists_ok:2,expect:[1,4],explicit:4,exporter_bas:[3,5],exporterbas:2,exportersconfig:1,extens:[1,4],extension_ind:1,extract:[1,4],extraction_mod:[],fab4219b:[],fail:1,fairli:4,fals:[1,2],few:4,field:[1,2,3,6],field_separ:1,file:[0,1,2,4,6],file_data:1,file_error:1,file_metadata:1,file_trait:[1,4],filenam:[1,2,4,6],filename_:[],filename_error:1,filename_field:1,filenotfounderror:[1,2],filepath:[1,2,6],filepath_rel:2,filespecificationbas:1,find:1,first:1,five:4,flake8:0,flask:[0,6],flassger:6,flip:4,folder:2,follow:[2,4],form:4,formal:4,format:[1,6],found:[1,2,6],frame:[1,4],frame_ind:1,frame_pad:1,framework:[2,4],free:4,freshli:4,from:[0,1,2,4,6],from_config:[1,2],from_json:1,frozen:0,full:4,fulli:0,fullpath:[],gener:[0,1,4,6],get:[0,1,4,6],get_app:[],get_app_command:0,get_architecture_diagram_command:0,get_asset_graph:6,get_asset_id:1,get_asset_nam:1,get_asset_path:1,get_bash_command:0,get_button:6,get_config_error:6,get_config_tab:6,get_configbar:6,get_container_id_command:0,get_coverage_command:0,get_dash_app:6,get_data_tab:6,get_datat:6,get_destroy_production_container_command:0,get_docker_command:0,get_docker_compose_command:0,get_docker_exec_command:0,get_docs_command:0,get_dropdown:6,get_dummy_el:6,get_file_trait:1,get_filename_metadata:[],get_filename_trait:1,get_fix_permissions_command:0,get_image_channel:1,get_image_height:1,get_image_id_command:0,get_image_width:1,get_info:0,get_initialization_error:6,get_json_editor:[],get_key_value_card:6,get_lab_command:0,get_lint_command:0,get_logo:[],get_package_command:0,get_production_container_command:0,get_production_image_command:0,get_publish_command:0,get_python_command:0,get_query_error:[],get_radon_metrics_command:0,get_read_error:6,get_remove_image_command:0,get_remove_pycache_command:0,get_requirements_command:0,get_search_error:6,get_searchbar:6,get_start_command:0,get_startup_paramet:[],get_stop_command:0,get_test_command:0,get_tox_command:0,get_trait:1,get_type_checking_command:0,get_update_error:6,girder:[1,2,4],girder_export:[3,5],girderconfig:[1,2],girderexport:2,git:4,github:4,give:1,given:[0,1,2,6],grammar:[1,3],grammat:4,graph:[3,6],greater:[1,4],green:4,greet:4,ground:4,group:[1,4],group_by_asset:1,halstead:3,handl:6,handle_data_error:6,has:[1,4,6],hash:1,have:[2,4],hb_parent:1,header:6,height:[1,4],help:4,here:4,hidebound:[0,1,2,4,6],hidebound_config:[4,6],hidebound_dir:[1,2],hidebound_directori:1,hidebound_parent_dir:[],hidebound_parent_directori:[],hideebiund_config:6,hierarch:4,highli:4,homogen:1,host:[2,4],how:[1,4],howev:[],html:[0,6],httperror:2,human:1,human_readable_delta:1,hyphen:4,id_:6,identifi:4,ignor:[],ignore_ord:[],illeg:[],imag:[0,1,4],implement:2,importantli:4,includ:[1,4],include_regex:1,index:[0,3],indic:4,individu:1,info:0,inform:[4,6],ingest:4,inherit:[],init:[1,2,4],init_button:[],initi:[1,4,6],input:6,insid:0,instal:3,instanc:[1,2,6],integr:0,intent:[],interpret:0,introduct:3,inttyp:[1,2],invalid:[1,2,4,6],ipv4typ:2,is_attribute_of:1,is_coordin:1,is_descriptor:1,is_directori:1,is_eq:1,is_extens:1,is_fil:1,is_fram:1,is_gt:1,is_hidebound_directori:1,is_homogen:1,is_in:1,is_lt:1,is_project:1,is_specification_fil:1,is_vers:1,item:1,its:[1,4],itself:4,jah:[],jaskldj78211:[],jinja2:6,join:4,jpeg:1,json:[1,2,4,6],jsondecodeerror:6,jump:4,jumping_v001:4,jumping_v001_f0001:4,jumping_v001_f0002:4,jumping_v001_f0003:4,junk:4,jupyt:0,kajsaks3:[],kei:[1,2,4,6],keyerror:6,known:4,kwarg:[1,2],lab:0,lambda:1,last:4,latest:4,layout:4,lazi:[1,2],least:4,legaci:4,legal:4,legal_field:1,length:[],less:1,let:4,letter:4,level:4,lexic:3,librari:[],like:4,line:4,link:4,lint:0,list:[0,1,4,6],list_all_fil:1,list_first_arg:1,listtyp:1,local:[1,2,4],locat:1,logo:[],look:4,lower:4,lowercas:[1,4],machin:4,maco:4,made:[1,4],mai:4,main:[0,4],maintain:[3,4],make:[1,4],mani:[],mappingproxi:[],mask:4,master:4,match:1,mean:4,meaning:[],meet:1,member:[],memori:[4,6],menu:[],mere:4,messag:1,metadata:[1,2,4],metdata:4,method:[1,2],metric:0,minut:4,misc:0,miss:[],mna:[],mnt:[],mode:[0,4],model:[1,2],modeltyp:1,modif:6,modul:[0,1,3],mongodb:4,more:4,move:4,multipl:[1,4],must:[1,2,4],mypi:0,n_click:[],name:[1,3,6],nerv:[],next:4,non:4,none:[0,1,2,6],notimplementederror:[1,2],now:4,nowrap:1,number:[1,4],object:[1,2],occcur:4,on_config_card_upd:6,on_create_button_click:[],on_datatable_upd:6,on_delete_button_click:[],on_ev:6,on_get_tab:6,on_init_button_click:[],on_json_editor_upd:[],on_session_data_upd:[],on_update_button_click:[],onc:4,one:[1,4,6],oneasset:[],onli:[1,4],open:0,oper:4,opion:4,option:[0,1,2,6],order:[1,4],orf:4,orient:4,origin:1,other:4,our:4,out:4,output:4,over:4,overview:3,packag:0,pad:4,page:[3,6],paht:2,pair:6,panda:1,param:1,paramet:[0,1,2,6],parent:4,pars:[1,6],parse_json_file_cont:6,parse_specif:1,parseexcept:1,parser:[3,5],part:[1,4],partial:[1,2],particular:4,patch_model:[1,2],patch_schema:[1,2],path:[1,2,6],pathlib:[1,2,6],per:[1,4,6],period:4,permiss:0,pip:[0,4],pipe:[],pixel:4,place:4,plai:4,playing_v001:4,playing_v001_f0001:4,playing_v001_f0002:4,playing_v001_f0003:4,playing_v002:4,playing_v002_f0001:4,playing_v002_f0002:4,playing_v002_f0003:4,plot:3,png:[1,4],popul:[1,4],port:2,postgr:4,preced:4,predic:1,present:1,presum:4,print:0,prior:4,privat:[],process:4,produc:4,product:0,profici:4,proj001:[],proj001_:[],project:[1,3],project_ind:1,properti:[1,6],prototyp:1,provid:0,publish:0,pull:4,put:4,pycach:0,pypars:1,pytest:0,python:[0,1,3],quadrupl:4,queri:[1,6],radon:0,rais:[1,2,6],raise_error:1,raw001:1,raw001_d:[],raw002:1,raw:[1,3,6],raw_cont:6,raw_data:[1,2],read:[1,4,6],readabl:1,realli:4,recommend:4,recurs:[0,1,2,4],recus:1,red:4,redefin:4,refer:[],regard:4,regex:1,rel:1,relative_path:1,reli:4,rememb:4,remov:[0,1],renam:4,render:6,render_cont:[],render_templ:6,repair:3,repo:0,repo_env:0,repo_path:0,repons:6,report:3,repositori:0,repres:6,request:6,requir:0,reserv:4,resolv:[0,1],respect:1,respons:[2,6],rest:4,result:4,retrun:[],return_item:1,revert:0,review:3,rgb:4,root:[0,1,2,4,6],root_dir:1,root_directori:1,root_id:2,root_typ:2,rough:4,rout:6,row:[1,4,6],run:[0,4],runtimeerror:1,sai:4,said:4,same:[1,4],save:1,scalar:1,schema:[1,2],schemat:[1,2,6],scope:[],search:[1,3,4,6],second:4,section:4,see:4,self:1,semant:3,sens:4,sentenc:4,separ:4,sepcif:[],seper:4,sequenc:[1,4],sequencespecificationbas:1,seri:4,serv:6,serve_stylesheet:6,server:[0,3,5],server_tool:[3,5],servic:[0,4],session:0,set:[1,4],setup_hidebound_directori:6,seven:4,sever:4,should:4,show:[],shut:0,signatur:1,silent:[],similarli:4,simpl:4,simplifi:4,singl:[1,2,4],singular:[],slightli:4,some:4,someth:4,sourc:[0,1,2,6],source_dir:1,space:4,spec001:4,spec001_d:4,spec002:4,spec002_d:4,special:3,specif:[3,4,5,6],specifi:4,specification_bas:[3,5],specification_class:1,specification_fil:1,specification_ind:1,specificationbas:1,specificationerror:[],split:1,sql:[1,4,6],standard:1,start:[0,1,4],state:[1,4],staticmethod:[],stdout:0,step:4,stipul:4,stop:1,stopwatch:1,storag:6,storage_typ:6,store:[4,6],str:[0,1,2,6],strict:[1,2,4],strign:[],string:[1,6],stringtyp:[1,2],structur:[0,1,3],stuff:4,stylesheet:6,subclass:[1,2],subpackag:4,succe:[],suffix:1,suppli:[1,2,6],support:4,sure:1,svg:0,syntax:3,system:0,tab:[4,6],tabbi:4,tabl:[4,6],take:4,tall:4,target:1,target_dir:1,technic:4,templat:6,term:4,test:[0,2,4,6],text:[1,4],than:[1,4],thats:1,thei:4,them:4,thenewflesh:4,therein:4,thi:[0,1,4],those:4,thought:4,three:[1,4],thu:4,time:1,timestamp:6,titl:6,tmp:4,to_prototyp:1,to_str:1,togeth:4,token:4,token_separ:1,tool:[3,4,5],toward:4,tox:0,trait:[3,4,5],transform:1,tripl:4,trusted_data:[1,2],try_:1,tupl:[1,6],two:4,type:[0,1,2,4,6],typeerror:6,typic:4,under:[0,1,2,4],underscor:4,undoc:[],union:[1,2,6],unment:4,updat:[1,3,6],update_button:[],upload:4,upon:4,upper:4,use:[1,4],used:[1,4,6],useless:4,user:4,using:[1,6],util:[],uuid:1,valid:[2,3,4,5,6],validate_each:1,validate_filepath:1,validationerror:1,valu:[1,4,6],valueerror:6,variabl:0,variou:4,version:[0,1,4],version_ind:1,version_pad:1,via:4,violat:4,visual:4,wai:4,walk:1,weak:[],web:4,well:4,what:4,whatev:[],when:[1,4],where:1,whether:1,which:[1,2,4],wide:4,width:[1,4],window:4,wip:4,wish:1,within:[1,2,4],word:4,work:0,workflow:3,workhors:4,working_directori:0,wrapper:6,write:[0,1,4,6],write_mod:[1,4],written:[0,1,6],wtf:4,xyz:4,yield:1,you:[1,4],zero:4},titles:["cli","core","exporters","Welcome to hidebound\u2019s documentation!","Introduction","&lt;no title&gt;","server"],titleterms:{"export":[2,4],For:4,api:[4,6],app:6,applic:4,architectur:3,asset:4,base:[],cli:0,client:[],compon:6,config:[1,4],convent:4,core:1,creat:4,data:4,databas:1,database_tool:1,delet:4,develop:4,diagnos:4,diagram:4,doc:4,docker:4,document:3,encourag:4,error:4,exampl:4,exporter_bas:2,field:4,girder_export:2,grammar:4,graph:4,hidebound:3,indic:3,instal:4,introduct:4,lexic:4,metadata:[],metric:3,name:4,nerv:[],overview:4,parser:1,project:4,python:4,repair:4,review:4,semant:4,server:6,server_tool:6,spec:[],special:4,specif:1,specification_bas:1,structur:4,syntax:4,tabl:3,tool:1,trait:1,updat:4,upload:[],util:[],valid:1,welcom:3,workflow:4}})