$.widget("fora.datatable", {

  options: {
    columns: [],
    actions: {
      view: false,
      edit: false,
      delete: false
    },
    uri: {
      retrieveEntries: "",
      retrieveEntry: "",
      deleteEntry: ""
    }
  },

  _draw: function() {
    var self = this;
    var html = "<table class='table table-hover'><thead><tr>";
    for(var i = 0; i < self.options.columns.length; ++i) {
      var column = self.options.columns[i];
      html += "<th>" + column.toUpperCase() + "</th>";
    }
    if (self.options.actions.view || self.options.actions.edit || self.options.actions.delete) {
      html += "<th>ACTIONS</th>";
    }
    html += "</tr></thead><tbody>";
    html += "</tbody></table>";
    html += "<div class='modal fade' id='modal-delete' role='dialog' aria-labelledby='modal-delete-title' aria-hidden='true'>"
    html += "<div class='modal-dialog'>";
    html += "<div class='modal-content'>";
    html += "<div class='modal-header'><h4 class='modal-title' id='modal-delete-title'>Delete</h4></div>";
    html += "<div class='modal-body'><p>You will delete a entry. Are you sure?</p></div>";
    html += "<div class='modal-footer'>";
    html += "<button type='button' class='btn btn-danger' data-dismiss='modal' aria-label='Delete'>DELETE</button>";
    html += "<button type='button' class='btn btn-primary' data-dismiss='modal' aria-label='Cancel'>CANCEL</button>";
    html += "</div>";
    html += "</div>";
    html += "</div>";
    html += "</div>";
    self.element.html(html);
  },
  _create: function() {
    var self = this;
    self.element.addClass("datatable");
    self._update();
  },

  _setOption: function(key, value) {
    var self = this;

    self.options[key] = value;
    self._update();
  },

  _update: function() {
    var self = this;

    self._draw();
    self._retrieveEntries();
  },

  _destroy: function() {
    var self = this;

    self.element.removeClass("datatable").html("");
  },

  _retrieveEntries: function() {
    var self = this;
    $.ajax({
      url: self.options.uri.retrieveEntries,
      type: "POST",
      data: JSON.stringify({
      }),
      contentType: 'application/json; charaset=utf-8',
      success: function(data) {
        if (data.status) {
          var tbody = self.element.find("table > tbody");
          tbody.html("");
          for(var i = 0; i < data.entries.length; ++i) {
            var entry = data.entries[i];
            var row = "<tr>";
            for(var j = 0; j < self.options.columns.length; ++j) {
              var column = self.options.columns[j];
              row += "<td>" + entry[column] + "</td>";
            }
            if (self.options.actions.view || self.options.actions.edit || self.options.actions.delete) {
              row += "<td>";
              if (self.options.actions.view) {
                row += "<a type='button' class='btn btn-default'>VIEW</a>";
              }
              if (self.options.actions.edit) {
                row += "<a type='button' class='btn btn-default'>EDIT</a>";
              }
              if (self.options.actions.delete) {
                row += "<a type='button' class='btn btn-danger' data-toggle='modal' data-target='#modal-delete'>DELETE</a>";
              }
              row += "</td>";
            }
            row += "</tr>";
            tbody.append(row);
          }
        }
      },
      error: function(data) {
      }
    });
  },

  _retrieveEntry: function() {
    var self = this;
    $.ajax({
      url: self.options.uri.retrieveEntry,
      type: "POST",
      data: JSON.stringify({
      }),
      contentType: 'application/json; charaset=utf-8',
      success: function(data) {
      },
      error: function(data) {
      }
    });
  },

  _deleteEntry: function() {
    var self = this;
  }

});
