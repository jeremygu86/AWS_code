!function(s){var i=function(i,a,t){var s=function template(a){var s=[],t={},d,i=a||{};return function(i){s.push('<div class="grid-submissions"><div data-js="in-progress-alert" class="bt3-alert bt3-alert-warning bt3-hide"><div class="title">Your submission is being graded.</div><div class="message">When your grade is ready, this page will automatically refresh and\nyour submission will appear below.\n</div></div><div data-js="submission-button-area" class="bt3-hide bt3-row"><div class="bt3-col-md-12"><div data-state-not="submitting">'),i?s.push('<div class="bt3-col-md-3"><div data-rc="PremiumGradingQuizButton" class="cozy"></div></div>'):s.push('<button data-js="create-submission-button" class="success cozy"><i class="cif-plus"></i>&nbsp; Create submission</button>'),s.push('</div><div data-state="submitting"><button data-js="cancel-submission-button" class="warning cozy"><i class="cif-times"></i>&nbsp; Cancel</button></div></div></div><div class="bt3-row"><div data-js="submitter-area" class="submitter-area bt3-hide"><div data-js="submitter-content" class="submitter-content"><h3>Upload Files and Submit</h3><div data-rc="GridSubmission"></div></div></div><div data-js="submissions-area" class="submissions-area bt3-col-md-12"><h3>Your Submissions</h3><div data-rc="Submissions" data-js="submission-history" class="bt3-hide"></div><div data-rc="NoSubmissions" data-js="no-submissions" class="no-submissions card-z0"></div><div data-js="submission-history-error" class="bt3-hide"></div></div></div></div>')}.call(this,"isPremiumGrading"in i?i.isPremiumGrading:"undefined"!=typeof isPremiumGrading?isPremiumGrading:void 0),s.join("")};return s};"function"==typeof define&&define.amd?define(["js/vendor/jade"],function(s){var a,t;return i(s,a,t)}):s.jade.templates["bundles.programming.views.gridSubmissions"]=i(s.jade.helpers)}(window);