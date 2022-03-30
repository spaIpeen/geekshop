jQuery(document).ready(function () {
    $('.users_list').on('click', 'input[type="checkbox"]', function () {
        let target_href = event.target;
        if (target_href) {
            $.ajax({
                url: "/admin/users/delete/" + target_href.name + "/",
                success: function (data) {
                    $('.users_list').html(data.result);
                    console.log('ajax done');
                },
            });
        }
        event.preventDefault();
    });
});