function htmlListTopicItem(entry) {
  var html = "<a href='/topic/" + entry.uuid + "' class='list-group-item'>";
  html += "<span class='badge'>" + 0 + " Unread Threads</span>";
  html += "<h4 class='list-group-item-heading'><i class='fa fa-comments'></i> " + entry.initial_thread.subject + "</h4>";
  html += "</a>";
  return html;
}

$(document).ready(function() {
  $.ajax({
    url: "?action=retrieve_topics",
    type: "POST",
    data: JSON.stringify({
    }),
    contentType: 'application/json; charaset=utf-8',
    success: function(data) {
      if (data.status) {
        var list = $("#panel-topics > #list-topic");
        for (var id in data.entries) {
          var entry = data.entries[id];
          var html = htmlListTopicItem(entry);
          list.append(html);
        }
        Holder.run();
      }
    }
  });

  $("#button-create-topic-submit").click(function() {
    var subject = $("#input-subject").val();
    var content = $("#textarea-content").val();
    var acceptPolicies = $("#checkbox-accept-policies").is(":checked");
    $.ajax({
      url: "?action=create_topic",
      type: "POST",
      data: JSON.stringify({
        subject: subject,
        content: content,
        acceptPolicies: acceptPolicies
      }),
      contentType: "application/json; charaset=utf-8",
      success: function(data) {
        if (data.status) {
        }
      }
    });
  });
});
