"use strict";define("bundles/programming/models/gradingStatuses",["require","exports","module","backbone"],function(require,exports,module){var Backbone=require("backbone"),e=Backbone.Model.extend({defaults:{typeName:null,definition:null},getPartForId:function getPartForId(t){var e=this.get("definition");if(!e)return null;var n=e.parts[t];return n&&n.definition}});module.exports=e});