 $(document).ready(function () {
            $('#tables').DataTable({
                    "lengthMenu" : [ [ 3, 5, 10, -1 ], [ 3, 5, 10, "All" ]],
                    "ajax" : {
                        url : '/Crawling',
                        type : 'POST',
                    },
                    columnDefs: [ {
                            targets: 1,
                            render : function(url){
                                return '<a href="'+url+'">'+url+'</a>'
                            }
				    }]
                });
  });