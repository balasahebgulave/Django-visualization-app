(function($) {

    'use strict';

    $(document).ready(function() {
        $.fn.datepicker.defaults.format = "yyyy/mm/dd";
        $('.js-datepicker').datepicker({
            autoclose: true
        });

        $('.input-group.date').datepicker({
            autoclose: true,
            todayHighlight: true
        });

        $('.input-daterange').datepicker({
            autoclose: true
        });

    });

})(window.jQuery);
