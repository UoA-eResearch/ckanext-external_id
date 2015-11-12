// Enable JavaScript's strict mode. Strict mode catches some common
// programming errors and throws exceptions, prevents some unsafe actions from
// being taken, and disables some confusing and bad JavaScript features.
"use strict";

ckan.module('external_id_form', function ($, _) {
  return {
    initialize: function () {
      var group = $('input#field-relation').parents('div.control-group');
      /* If the external ID is already set, set the select list to manual
         and display the current value. Otherwise, default to the first
         available external ID provider, and hide the custom input
      */
      if ($('input#field-relation').val() == '' &&
          $('select#field-relation-select').val() != 'manual') {
        group.hide();
      } else {
        $('select#field-relation-select').val('manual');
      }
      $('select#field-relation-select').change(function(event) {
        var new_val = $(this).val();
        if (new_val === 'manual') {
          // If the user selects manual entry - display an input to receive it
          group.show();
        } else {
          group.hide();
          $('input#field-relation').val(new_val);
        }
      });
    }
  };
});