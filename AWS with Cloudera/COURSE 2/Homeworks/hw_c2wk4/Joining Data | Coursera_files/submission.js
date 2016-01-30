"use strict";define("bundles/programming/viewModels/submission",["require","exports","module","q","underscore","bundles/phoenix/lib/viewModel","bundles/phoenix/template/models/userIdentity","bundles/programming/api/filesSubmissions","bundles/programming/api/filesWorkspaceParts","bundles/programming/promises/filesWorkspace","bundles/programming/stores/submissionSummariesStore"],function(require,exports,module){var e=require("q"),_=require("underscore"),o=require("bundles/phoenix/lib/viewModel"),i=require("bundles/phoenix/template/models/userIdentity"),t=require("bundles/programming/api/filesSubmissions"),r=require("bundles/programming/api/filesWorkspaceParts"),n=require("bundles/programming/promises/filesWorkspace"),s=require("bundles/programming/stores/submissionSummariesStore"),a=o.extend({defaults:{filesWorkspace:null,submissionHistory:null},initialize:function initialize(e){_(this).bindAll("loadSubmissionHistory","onLoadFilesWorkspaceSuccess","onLoadFilesWorkspaceError","onLoadSubmissionHistorySuccess","onLoadSubmissionHistoryError","onSubmitSuccess","onSubmitError","onPostUploadPartSuccess","onPostUploadPartError"),_(this).extend(_(e).pick("itemMetadata","learnerAssignment","inputViewModel","verificationDisplay","isVerifiable")),s.on("update",this.onLoadSubmissionHistorySuccess),s.on("updateError",this.onLoadSubmissionHistoryError)},loadFileUploadParts:function loadFileUploadParts(){if("files"!==this.learnerAssignment.submissionBuilderSchema.get("typeName"))return e({});var s={itemMetadata:this.itemMetadata,courseId:this.itemMetadata.get("course").get("id"),itemId:this.itemMetadata.get("id")};return n(s).then(this.onLoadFilesWorkspaceSuccess,this.onLoadFilesWorkspaceError)},loadSubmissionHistory:function loadSubmissionHistory(){s.load({itemMetadata:this.itemMetadata,userId:i.get("id"),courseId:this.itemMetadata.get("course").get("id"),itemId:this.itemMetadata.get("id")})},submit:function submit(s){this.inputViewModel.set("inputDisabled",!0);var e={courseId:this.itemMetadata.get("course").get("id"),itemId:this.itemMetadata.get("id"),itemMetadata:this.itemMetadata,versionId:this.get("filesWorkspace").get("versionId")};return s&&(e.verifiableId=s),t.submit(e).then(this.onSubmitSuccess,this.onSubmitError)},postUploadPart:function postUploadPart(s){return r.create(s).then(this.onPostUploadPartSuccess,this.onPostUploadPartError)["catch"](function(s){throw console.error("Error posting upload part:",s&&s.stack?s.stack:s),s})},onLoadFilesWorkspaceSuccess:function onLoadFilesWorkspaceSuccess(s){this.set("filesWorkspace",s)},onLoadFilesWorkspaceError:function onLoadFilesWorkspaceError(s){if(!s.responseJSON)throw s;console.error("onLoadFilesWorkspaceError",s.responseJSON)},onLoadSubmissionHistorySuccess:function onLoadSubmissionHistorySuccess(s){this.set("submissionHistory",s)},onLoadSubmissionHistoryError:function onLoadSubmissionHistoryError(s){if(!s.responseJSON)throw s;console.error("onLoadSubmissionHistoryError",s.responseJSON)},onSubmitSuccess:function onSubmitSuccess(){var s=function(){this.inputViewModel.set("inputDisabled",!1)}.bind(this);return this.loadFileUploadParts().then(this.loadSubmissionHistory).then(s,s)},onSubmitError:function onSubmitError(s){if(this.inputViewModel.set("inputDisabled",!1),!s.responseJSON)throw s;console.error("onSubmitError",s.responseJSON)},onPostUploadPartSuccess:function onPostUploadPartSuccess(){return this.loadFileUploadParts()},onPostUploadPartError:function onPostUploadPartError(s){if(!s.responseJSON)throw s;console.error("onPostUploadPartError",s.responseJSON)}});module.exports=a});