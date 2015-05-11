$.widget("fora.datatable", {

  options: {
    columns: [],
    actions: {
      create: false,
      view: false,
      edit: false,
      delete: false
    },
    modals: {
      create: true,
      view: true,
      edit: true,
      delete: true
    },
    uri: {
      retrieveEntries: "",
      retrieveEntry: "",
      viewEntry: "",
      createEntry: "",
      editEntry: "",
      deleteEntry: ""
    }
  },

  _draw: function() {
    var self = this;
    var html = "";
    html += "<div id='alert-datatable-error-create-entry' class='alert alert-danger' role='alert' style='display: none'>Error occurs during entry create.</div>";
    if (self.options.actions.create) {
      if (self.options.modals.create) {
        html += "<button type='button' class='btn btn-default pull-right' data-toggle='modal' data-target='#modal-create'>CREATE</button>";
      } else {
        html += "<a type='button' class='btn btn-default pull-right' href='" + self.options.uri.createEntry + "'>CREATE</a>";
      }
    }
    html += "<table class='table table-hover'><thead><tr>";
    for(var i = 0; i < self.options.columns.length; ++i) {
      var column = self.options.columns[i];
      html += "<th>" + column.toUpperCase() + "</th>";
    }
    if (self.options.actions.view || self.options.actions.edit || self.options.actions.delete) {
      html += "<th>ACTIONS</th>";
    }
    html += "</tr></thead><tbody>";
    html += "</tbody></table>";
    if (self.options.actions.create && self.options.modals.create) {
      html += "<div class='modal fade' id='modal-create' role='dialog' aria-labelledby='modal-create-title' aria-hidden='true'>"
      html += "<div class='modal-dialog'>";
      html += "<div class='modal-content'>";
      html += "<div class='modal-header'><h4 class='modal-title' id='modal-create-title'>Create</h4></div>";
      html += "<div class='modal-body'></div>";
      html += "<div class='modal-footer'>";
      html += "<button type='button' class='btn btn-success' data-dismiss='modal' aria-label='Submit'>SUBMIT</button>";
      html += "<button type='button' class='btn btn-primary' data-dismiss='modal' aria-label='Cancel'>CANCEL</button>";
      html += "</div>";
      html += "</div>";
      html += "</div>";
      html += "</div>";
    }
    if (self.options.actions.view && self.options.modals.view) {
      html += "<div class='modal fade' id='modal-view' role='dialog' aria-labelledby='modal-view-title' aria-hidden='true'>"
      html += "<div class='modal-dialog'>";
      html += "<div class='modal-content'>";
      html += "<div class='modal-header'><h4 class='modal-title' id='modal-view-title'>View</h4></div>";
      html += "<div class='modal-body'></div>";
      html += "<div class='modal-footer'>";
      html += "<button type='button' class='btn btn-primary' data-dismiss='modal' aria-label='Close'>CLOSE</button>";
      html += "</div>";
      html += "</div>";
      html += "</div>";
      html += "</div>";
    }
    if (self.options.actions.edit && self.options.modals.edit) {
      html += "<div class='modal fade' id='modal-edit' role='dialog' aria-labelledby='modal-edit-title' aria-hidden='true'>"
      html += "<div class='modal-dialog'>";
      html += "<div class='modal-content'>";
      html += "<div class='modal-header'><h4 class='modal-title' id='modal-edit-title'>Edit</h4></div>";
      html += "<div class='modal-body'></div>";
      html += "<div class='modal-footer'>";
      html += "<button type='button' class='btn btn-success' data-dismiss='modal' aria-label='Submit'>SUBMIT</button>";
      html += "<button type='button' class='btn btn-primary' data-dismiss='modal' aria-label='Cancel'>CANCEL</button>";
      html += "</div>";
      html += "</div>";
      html += "</div>";
      html += "</div>";
    }
    if (self.options.actions.delete && self.options.modals.delete) {
      html += "<div class='modal fade' id='modal-delete' role='dialog' aria-labelledby='modal-delete-title' aria-hidden='true'>"
      html += "<div class='modal-dialog'>";
      html += "<div class='modal-content'>";
      html += "<div class='modal-header'><h4 class='modal-title' id='modal-delete-title'>Delete</h4></div>";
      html += "<div class='modal-body'><p>You will delete a entry. Are you sure?</p></div>";
      html += "<div class='modal-footer'>";
      html += "<button id='modal-delete-confirm' type='button' class='btn btn-danger' data-dismiss='modal' aria-label='Delete'>DELETE</button>";
      html += "<button type='button' class='btn btn-primary' data-dismiss='modal' aria-label='Cancel'>CANCEL</button>";
      html += "</div>";
      html += "</div>";
      html += "</div>";
      html += "</div>";
    }
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
    if (self.options.actions.delete && self.options.modals.delete) {
      $("#modal-delete-confirm").click(function( event ) {
        event.preventDefault();
        var identity = $(this).data("identity");
        self._deleteEntry(identity);
      });
    }
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
                if (self.options.modals.view) {
                  row += "<a type='button' class='btn btn-info' data-toggle='modal' data-target='#modal-view'>VIEW</a>";
                } else {
                  var href = self.options.uri.viewEntry.replace(/{identity}/i, entry['identity']);
                  row += "<a type='button' class='btn btn-info' href='" + href + "'>VIEW</a>";
                }
              }
              if (self.options.actions.edit) {
                if (self.options.modals.edit) {
                  row += "<a type='button' class='btn btn-default' data-toggle='modal' data-target='#modal-edit'>EDIT</a>";
                } else {
                  var href = self.options.uri.editEntry.replace(/{identity}/i, entry['identity']);
                  row += "<a type='button' class='btn btn-default' href='" + href + "'>EDIT</a>";
                }
              }
              if (self.options.actions.delete) {
                if (self.options.modals.delete) {
                  row += "<a type='button' class='btn btn-danger action-delete' data-identity='" + entry['identity'] + "'>DELETE</a>";
                } else {
                  var href = self.options.uri.deleteEntry.replace(/{identity}/i, entry['identity']);
                  row += "<a type='button' class='btn btn-danger' href='" + href + "'>DELETE</a>";
                }
              }
              row += "</td>";
            }
            row += "</tr>";
            tbody.append(row);
          }
          if (self.options.actions.delete && self.options.modals.delete) {
            $(".action-delete").click(function( event ) {
              event.preventDefault();
              var identity = $(this).data("identity");
              $("#modal-delete-confirm").data("identity", identity);
              $("#modal-delete").modal("show");
            });
          }
        }
      },
      error: function(data) {
      }
    });
  },

  _retrieveEntry: function(identity) {
    var self = this;
    $.ajax({
      url: self.options.uri.retrieveEntry,
      type: "POST",
      data: JSON.stringify({
        identity: identity
      }),
      contentType: 'application/json; charaset=utf-8',
      success: function(data) {
      },
      error: function(data) {
      }
    });
  },

  _deleteEntry: function(identity) {
    var self = this;
    $.ajax({
      url: self.options.uri.deleteEntry,
      type: "POST",
      data: JSON.stringify({
        identity: identity
      }),
      contentType: 'application/json; charaset=utf-8',
      success: function(data) {
        if (data.status) {
          self._retrieveEntries();
        } else {
          $("#alert-datatable-error-create-entry").show();
        }
      },
      error: function(data) {
        $("#alert-datatable-error-create-entry").show();
      }
    });
  }

});
