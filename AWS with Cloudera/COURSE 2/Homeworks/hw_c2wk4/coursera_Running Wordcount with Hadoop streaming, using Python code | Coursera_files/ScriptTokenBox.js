"use strict";define("bundles/programming/components/ScriptTokenBox",["require","exports","module","moment","react-with-addons","underscore","bundles/naptime/handleResponse","bundles/phoenix/components/Modal","bundles/phoenix/components/OrigamiRegion","bundles/phoenix/template/models/userIdentity","bundles/verification/viewModels/verificationModule","bundles/verification/views/verificationModule","js/lib/assert","js/lib/coursera.react-intl","i18n!nls/programming","bundles/programming/api/gradedScriptTokens","bundles/programming/api/ungradedScriptTokens","css!bundles/styleguide/learnerApp/cards.css","css!bundles/programming/components/__styles__/ScriptTokenBox.css"],function(require,exports,module){var l=require("moment"),e=require("react-with-addons"),_=require("underscore"),d=require("bundles/naptime/handleResponse"),m=require("bundles/phoenix/components/Modal"),r=require("bundles/phoenix/components/OrigamiRegion"),o=require("bundles/phoenix/template/models/userIdentity"),a=require("bundles/verification/viewModels/verificationModule"),s=require("bundles/verification/views/verificationModule"),i=require("js/lib/assert"),c=require("js/lib/coursera.react-intl"),n=c.FormattedMessage,t=require("i18n!nls/programming"),p=require("bundles/programming/api/gradedScriptTokens"),u=require("bundles/programming/api/ungradedScriptTokens");require("css!bundles/styleguide/learnerApp/cards.css"),require("css!bundles/programming/components/__styles__/ScriptTokenBox.css");var h={gradedProgramming:p,ungradedProgramming:u},g=e.createClass({displayName:"ScriptTokenBox",propTypes:{itemMetadata:e.PropTypes.object.isRequired,verificationDisplay:e.PropTypes.object.isRequired},getInitialState:function getInitialState(){return{state:"ready",token:{},currentTime:Date.now()}},componentDidMount:function componentDidMount(){var e=this.props.itemMetadata.getTypeName();this.api=h[e],i(this.api,"Unknown assignment type: "+e),this.currentTimeInterval=setInterval(this.updateCurrentTime,1e3),this.loadToken()},componentWillUnmount:function componentWillUnmount(){clearInterval(this.currentTimeInterval)},isGraded:function isGraded(){return"gradedProgramming"===this.props.itemMetadata.getTypeName()},isVerifiable:function isVerifiable(){return this.props.verificationDisplay.shouldPromptForVerification()},requiresVerification:function requiresVerification(){return this.isGraded()&&this.isVerifiable()},updateCurrentTime:function updateCurrentTime(){this.setState({currentTime:Date.now()})},loadToken:function loadToken(){this.setState({state:"getting"}),this.api.get(this.props.itemMetadata).then(d).then(function(e){return e.elements[0]}).then(this.onReceiveToken,this.onTokenNotFound).done()},verifyAndGenerateToken:function verifyAndGenerateToken(e){e&&e.preventDefault(),this.requiresVerification()?(this.verificationViewModel=new a({verificationDisplay:this.props.verificationDisplay,metadata:this.props.itemMetadata}),this.verificationViewModel.on("verificationComplete",this.onVerificationComplete),this.setState({isVerifying:!0})):this.generateToken()},generateToken:function generateToken(e){this.setState({state:"generating"}),this.api.newToken(this.props.itemMetadata,e).then(this.onTokenGenerated,this.onFailedTokenGeneration)},onVerificationModalClose:function onVerificationModalClose(){this.setState({isVerifying:!1})},onVerificationComplete:function onVerificationComplete(e){e&&e.hasVerified===!0?this.generateToken(this.verificationViewModel.get("verifiableId")):this.generateToken(),this.setState({isVerifying:!1})},onReceiveToken:function onReceiveToken(e){this.setState({state:"displaying",token:e})},onTokenNotFound:function onTokenNotFound(){this.requiresVerification()?this.setState({state:"displaying"}):this.generateToken()},onTokenGenerated:function onTokenGenerated(){this.loadToken()},onFailedTokenGeneration:function onFailedTokenGeneration(e){this.setState({state:"error",error:e})},render:function render(){var a=this.state,c=a.state,i=a.token,p=a.currentTime,u=a.isVerifying,h=a.error,d=i&&i.expiresAt-p<=0;return e.createElement("div",{className:"rc-ScriptTokenBox well card-z1"},e.createElement("h3",{className:"head-2-text"},t("How to submit")),e.createElement("p",null,t("Copy the token below and run the submission script included in the assignment download.\n          When prompted, use your email address")," ",e.createElement("b",null,o.get("email_address")),"."),e.createElement("div",{className:"token-area bt3-text-center"},_(["getting","generating"]).contains(c)&&e.createElement("p",null,t("Loading token...")),_(["displaying"]).contains(c)&&e.createElement("div",null,i&&e.createElement("div",null,(!i.expiresAt||!d)&&e.createElement("h4",null,i.secret),i.expiresAt&&!d&&e.createElement("p",{className:"caption-text"},e.createElement(n,{message:t("This token expires in {expirationTime}"),expirationTime:l(i.expiresAt).fromNow(!0)})),i.expiresAt&&d&&e.createElement("p",{className:"caption-text"},t("Your token expired"))),e.createElement("p",null,e.createElement("a",{href:"#",onClick:this.verifyAndGenerateToken},t("Generate new token")))),_(["error"]).contains(c)&&e.createElement("div",null,e.createElement("p",null,e.createElement(n,{message:t("There was an error getting your token: {error}"),error:h})," ",e.createElement("a",{href:"#",onClick:this.verifyAndGenerateToken},"Click here to try to get it again")))),e.createElement("p",null,t("Your submission token is unique to you and should not be shared with anyone.\n          You may submit as many times as you like.")),u&&e.createElement(m,{modalName:"Programming Assignment Token",handleClose:this.onVerificationModalClose},e.createElement("h2",{className:"head-2-text"},t("Verify to Generate Token")),e.createElement(r,{renderOnce:!0,ViewClass:s,viewOptions:{verificationViewModel:this.verificationViewModel}})))}});module.exports=g});