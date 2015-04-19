$(document).ready(function() {
  $("#form-user-registration > .form-group > #input-email-address").change(function() {
    var email_address = $(this).val();
  });
  $("#submit-form-user-registration").click(function( event ) {
    event.preventDefault();
    var email_address = $("#form-user-registration > .form-group > #input-email-address").val();
    var username = $("#form-user-registration > .form-group > #input-username").val();
    var password = $("#form-user-registration > .form-group > #input-password").val();
    var confirmPassword = $("#form-user-registration > .form-group > #input-confirm-password").val();
    var acceptPolicies = $("#checkbox-accept-policies").is(":checked");

    if (password == confirmPassword && acceptPolicies) {
      $.ajax({
        url: "?action=create_user",
        type: "POST",
        data: JSON.stringify({
          "email_address": email_address,
          "username": username,
          "password": password,
          "acceptPolicies": acceptPolicies
        }),
        contentType: 'application/json; charaset=utf-8',
        success: function(data) {

        }
      });
    }
  });
});
