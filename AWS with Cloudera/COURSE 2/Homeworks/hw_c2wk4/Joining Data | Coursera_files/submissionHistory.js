"use strict";define("bundles/programming/components/SubmissionHistory",["require","exports","module","react-with-addons","underscore","bundles/phoenix/components/Time","i18n!nls/programming","bundles/programming/models/submissionHistory","css!bundles/programming/components/__styles__/SubmissionHistory.css"],function(require,exports,module){var e=require("react-with-addons"),_=require("underscore"),t=require("bundles/phoenix/components/Time"),s=require("i18n!nls/programming"),n=require("bundles/programming/models/submissionHistory");require("css!bundles/programming/components/__styles__/SubmissionHistory.css");var n=e.createClass({displayName:"SubmissionHistory",propTyps:{submissions:e.PropTypes.instanceOf(n).isRequired,columns:e.PropTypes.arrayOf(e.PropTypes.shape({title:e.PropTypes.string.isRequired,value:e.PropTypes.func.isRequired}))},getDefaultProps:function getDefaultProps(){return{columns:[{title:s("Date and time of submission"),align:"left",value:function value(s){return e.createElement(t,{time:s.get("submittedAt")})}},{title:s("Passed?"),align:"center",value:function value(e){return s(e.get("evaluation").isPassed()?"Yes":"No")}},{title:s("Total score"),align:"right",value:function value(n){var s=n.get("evaluation");return e.createElement("span",null,s.get("score")," / ",s.get("maxScore"))}}]}},render:function render(){var n=this;return e.createElement("div",{className:"rc-SubmissionHistory"},e.createElement("h3",null,s("Submission History")),e.createElement("table",{className:"table"},e.createElement("thead",null,this.props.columns.map(function(s){return e.createElement("th",{key:s.title,className:"align-"+s.align},s.title)})),e.createElement("tbody",null,this.props.submissions.map(function(s){return e.createElement("tr",{key:s.get("id")},n.props.columns.map(function(n){return e.createElement("td",{key:n.title,className:"align-"+n.align},n.value(s))}))}))))}});module.exports=n});