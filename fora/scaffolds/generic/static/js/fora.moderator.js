$(document).ready(function() {
  $("#button-login-submit").click(function( event ){
    event.preventDefault();
    var form = $("#form-login");
    var identity = form.find("#input-identity").val();
    var password = form.find("#input-password").val();
    $.ajax({
      url: "/admin?action=login_moderator",
      type: "POST",
      data: JSON.stringify({
        "identity": identity,
        "password": password
      }),
      contentType: 'application/json; charaset=utf-8',
      success: function(data) {
        if (data.status) {
          $("#alert-login-invalid-credential").hide();
          $("#alert-login-success").show();
          document.location.reload();
        } else {
          $("#alert-login-success").hide();
          $("#alert-login-invalid-credential").show();
        }
      }
    });
  });

  $("#nav-logout").click(function( event ){
    event.preventDefault();
    $.ajax({
      url: "/admin?action=logout_moderator",
      type: "POST",
      data: JSON.stringify({
      }),
      contentType: 'application/json; charaset=utf-8',
      success: function(data) {
        if (data.status) {
          document.location.reload();
        }
      }
    });
  });
});
