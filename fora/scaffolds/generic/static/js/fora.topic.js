function htmlListThreadItem(entry) {
  var html = "<div href='/thread/" + entry.uuid + "' class='list-group-item'>";

  html += "<div class='row'>";
  html += "<div class='col-xs-3 col-sm-2 col-md-1'>";
  html += "<img class='img-responsive' data-src='holder.js/168x168/auto/social/font:FontAwesome/text:&#xF007;/size:64' alt='Avatar'>";
  html += "</div>";
  html += "<div class='col-xs-9 col-sm-10 col-md-11'>";
  html += "<h4 class='list-group-item-heading'>" + entry.subject + "</h4>";
  html += "<p class='list-group-item-text'>" + entry.content + "</p>";
  html += "</div>";
  html += "</div>";

  html += "<div class='row'>";
  html += "<div class='col-xs-3 col-sm-2 col-md-1'>";
  if (entry.is_anonymous) {
    html += "<h5 style='text-align:center;'><span>" + entry.author + "</span></h5>";
  } else {
    html += "<h5 style='text-align:center;'><a href='/user/" + entry.author + "'>" + entry.username + "</a></h5>";
  }
  html += "</div>";
  html += "<div class='col-xs-9 col-sm-10 col-md-11'>";
  html += "<h6 style='text-align:right;'><a href='/thread/" + entry.uuid + "'>#" + entry.id + "</a> " + entry.update_date + "</h6>";
  html += "</div>";
  html += "</div>";

  html += "</div>";
  return html;
}

$(document).ready(function() {
  $.ajax({
    url: "?action=retrieve_threads",
    type: "POST",
    data: JSON.stringify({
    }),
    contentType: 'application/json; charaset=utf-8',
    success: function(data) {
      if (data.status) {
        var list = $("#panel-threads > #list-thread");
        for (var uuid in data.entries) {
          var entry = data.entries[uuid];
          var html = htmlListThreadItem(entry);
          list.append(html);
        }
        Holder.run();
      }
    }
  });

  $("#button-reply-topic-submit").click(function() {
    var subject = $("#input-subject").val();
    var content = $("#textarea-content").val();
    var acceptPolicies = $("#checkbox-accept-policies").is(":checked");
    $.ajax({
      url: "?action=reply_topic",
      type: "POST",
      data: JSON.stringify({
        subject: subject,
        content: content,
        acceptPolicies: acceptPolicies
      }),
      contentType: "application/json; charaset=utf-8",
      success: function(data) {
        if (data.status) {
          document.location.reload();
        } else {
        }
      }
    });
  });
});
