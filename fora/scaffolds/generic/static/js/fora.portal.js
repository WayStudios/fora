function htmlListForumItem(entry) {
  var html = "<a href='/forum/" + entry.uuid + "' class='list-group-item'>";
  html += "<h4 class='list-group-item-heading'>" + entry.title + "</h4>";
  html += "<p class='list-group-item-text'>" + entry.description + "</p>";
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
      if (data.status) {
        var list = $("#panel-forums > #list-forum");
        for (var uuid in data.entries) {
          var entry = data.entries[uuid];
          var html = htmlListForumItem(entry);
          list.append(html);
        }
      }
    }
  });
});
