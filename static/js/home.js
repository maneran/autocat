!function(){function a(){d.modal("hide"),$pdk.controller.resetPlayer(),d.find("#videoPlayer").html("")}function b(b,c,e,f,g){var h={accountPid:RottenTomatoes.thirdParty&&RottenTomatoes.thirdParty.mpx.accountPid||"",playerPid:RottenTomatoes.thirdParty&&RottenTomatoes.thirdParty.mpx.playerPid||"",accountId:RottenTomatoes.thirdParty&&RottenTomatoes.thirdParty.mpx.accountId||""};d.find("#videoPlayer").html('<iframe class="player" src="//player.theplatform.com/p/'+h.accountPid+"/"+h.playerPid+"/select/media/guid/"+h.accountId+"/"+b+"?autoPlay="+f+g+'&params=manifest%3Dm3u%26sst%3Dtrue%26debug%3Dtrue%26policy%3D9369485" onload="$pdk.bind(this, true); $pdk.controller.setIFrame(this, true);"allowfullscreen="" webkitallowfullscreen="" mozallowfullscreen="" oallowfullscreen="" msallowfullscreen=""frameborder="0"></iframe>'),d.modal(),d.on("hidden.bs.modal",a),dataLayer.push({event:"ModalTrailer",title:e})}function c(b){d=b,$(".closebutton").on("click",a),$(".closeBtn").on("click",a)}var d=null;RottenTomatoes.trailerModal={init:c,openNewModal:b}}(),function(){function a(a,b,c){e.modal(),$("#iframeVideoPlayer").attr("src",a),f.attr("content",g+",minimum-scale=1,maximum-scale=1,user-scalable=no"),e.find(".modal-dialog").append('<div class="modal-link-text"><a target="_blank" class="modal-link-url" style="color:#FFFFFF" href="'+c+'"></a></div>'),e.find(".modal-link-url").text(b)}function b(){$("#newIframeTrailerModal").modal("hide")}function c(){$("#iframeVideoPlayer").attr("src","about:blank"),f.attr("content",g)}function d(a){e=a,f=$('meta[name="viewport"]'),g=f.attr("content"),e.on("hidden.bs.modal",c),$(".closebutton").on("click",b)}var e=null,f=null,g=null;RottenTomatoes.iFrameTrailerModal={init:d,openIframeModal:a}}(),function(){function a(a){a.preventDefault();var b=$(a.currentTarget);e?RottenTomatoes.iFrameTrailerModal.openIframeModal(b.attr("data-trailer-url"),b.data("sponsoredText"),b.data("sponsoredUrl")):f=function(){RottenTomatoes.iFrameTrailerModal.openIframeModal(b.attr("data-trailer-url"),b.data("sponsoredText"),b.data("sponsoredUrl"))}}function b(a){a.preventDefault();var b=$(a.currentTarget),e="";b.data("mpx-fwsite")&&(e="&fwsitesection="+b.data("mpx-fwsite")),c?RottenTomatoes.trailerModal.openNewModal(b.data("video-id"),b.data("thumbnail"),b.data("title"),!0,e):d=function(){RottenTomatoes.trailerModal.openNewModal(b.data("video-id"),b.data("thumbnail"),b.data("title"),!0,e)}}var c=!1,d=null,e=!1,f=null;!function(){RottenTomatoes.trailerModal.init($("#newTrailerModal")),c=!0,d&&(d(),d=null),RottenTomatoes.iFrameTrailerModal.init($("#newIframeTrailerModal")),e=!0,f&&(f(),f=null),$(".trailer_play_action_button").on("click",b),$(".featured_video_play_action_button").on("click",a)}()}(),function(){var a,b={ACTIVE_SLIDE:".headlineItem.item.active",LAZY_LOAD:".js-lazyLoad",SLIDE:".carousel.slide",HEADLINE_ITEM:".carousel .headlineItem.item"},c=RottenTomatoes.lazyLoad.revealImage,d=0;$(b.SLIDE).on("slide.bs.carousel",function(e){d!==$(b.HEADLINE_ITEM).length-1&&("right"===e.direction?(a=0===d?$(b.HEADLINE_ITEM).last():$(b.ACTIVE_SLIDE).prev(),d--):(a=$(b.ACTIVE_SLIDE).next(),d++),c(a.find(b.LAZY_LOAD)))}),$(b.SLIDE).on("slid.bs.carousel",function(){c($(b.ACTIVE_SLIDE).find(b.LAZY_LOAD))}),c($(b.ACTIVE_SLIDE).find(b.LAZY_LOAD))}();