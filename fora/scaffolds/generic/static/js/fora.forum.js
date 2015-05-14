function htmlListForumItem(entry) {
  var html = "<a href='/forum/" + entry.uuid + "' class='list-group-item'>";
  html += "<h4 class='list-group-item-heading'>" + entry.title + "</h4>";
  html += "<p class='list-group-item-text'>" + entry.description + "</p>";
  html += "</a>";
  return html;
}

function htmlListTopicItem(entry) {
  var html = "<a href='/topic/" + entry.uuid + "' class='list-group-item'>";
  html += "<h4 class='list-group-item-heading'><i class='fa fa-comments'></i> " + entry.initial_thread.subject + "</h4>";
  html += "</a>";
  return html;
}

$(document).ready(function() {
  $.ajax({
    url: "?action=retrieve_forums",
    type: "POST",
    data: JSON.stringify({
    }),
    contentType: 'application/json; charaset=utf-8',
    success: function(data) {
      if (data.status && data.length > 0) {
        var list = $("#panel-forum > #list-forum");
        for (var id in data.entries) {
          var entry = data.entries[id];
          var html = htmlListForumItem(entry);
          list.append(html);
        }
        list.show();
        Holder.run();
      }
    }
  });

  $.ajax({
    url: "?action=retrieve_topics",
    type: "POST",
    data: JSON.stringify({
    }),
    contentType: 'application/json; charaset=utf-8',
    success: function(data) {
      if (data.status && data.length > 0) {
        var list = $("#panel-forum > #list-topic");
        for (var id in data.entries) {
          var entry = data.entries[id];
          var html = htmlListTopicItem(entry);
          list.append(html);
        }
        list.show();
        Holder.run();
      } else {
        $("#alert-list-topic-empty").show();
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
          document.location.reload();
        }
      }
    });
  });
});
