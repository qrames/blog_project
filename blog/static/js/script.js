$(document).ready(function() {
    // Stuff to do as soon as the DOM is ready
    $('#datepicker').datepicker({
        language: 'fr-FR',
        format: 'dd/mm/yyyy',
        autoShow: true
    });

    $('[data-toggle="datepicker"]').on('pick.datepicker', function(e) {
        // alert(e.date.toLocaleDateString() );
        $('[data-toggle="datepicker_input"]').val( e.date.toLocaleDateString());
        // alert($('[data-toggle="datepicker_input"]').val());
        $('#dateForm').submit();
    });


});
