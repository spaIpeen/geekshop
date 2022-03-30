jQuery(document).ready(function () {
    $('.categories_list').on('click', 'input[type="checkbox"]', function () {
        let target_href = event.target;
        if (target_href) {
            $.ajax({
                url: "/admin/categories/delete/" + target_href.name + "/",
                success: function (data) {
                    $('.categories_list').html(data.result);
                    console.log('ajax done');
                },
            });
        }
        event.preventDefault();
    });
});