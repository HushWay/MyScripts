function getResult(keyword) {
    // window.location.href = "https://pm.yuntsg.com/searchList.html";
    //当前页面的再次检索
    var ajaxTimeOut = $.ajax({
        url: './search/search',
        type: 'post',
        dataType: 'json',
        async: true,
        timeout: '60000',
        xhrFields: { withCredentials: true },
        data: {
            term: keyword,//检索词+下拉框的拼接
            sort: '',//排序
            format: '',//显示模式
            filter: [].join(','),//左侧的筛选
            impactIf: '',
            impact: '',//cs影响因子
            sjr: '',//威望指数
            fenqu: '',//中科院分区
            total: '',//被引次数
            alt: '',//替代计量
            jabbr: '',//期刊
            size: 20,//每页的条数
            page: 1,//页码
            num: 1,
            order: 1,
            // pos:'',//此参数暂时不传
            exclude: '0',
            reKey: 'e6b3cf23be217662fa2ff935acb43fb8',
            pmidListIndex: '',
            pmidListKey: '',
            linkname: '',
        },
        beforeSend: function () {
            index = layer.load(3, { shade: [0.5, '#ffffff'] });
        },
        complete: function (XMLHttpRequest, status) {
            if (status == 'timeout') {
                ajaxTimeOut.abort();
                var timeIndex = layer.confirm('抱歉，请求超时', {
                    btn: ['重新发送'] //按钮
                }, function () {
                    layer.close(timeIndex);
                    getData(keyword);
                });
            } else {
                goToLogin(XMLHttpRequest, status);
            }
        },
        success: function (data) {
            layer.close(index);
            if (data['code'] == 0) {
                if (data['data']) {
                    var jlTerm = '';
                    if (data['data']['term'] && data['data']['term'].indexOf('+') > -1) {
                        jlTerm = data['data']['term'].replace(/\+/g, " ");
                    } else {
                        jlTerm = data['data']['term'];
                    }
                    terms = jlTerm;
                    $('.keyWord').val(decodeURIComponent(terms));

                    num = data['data']['num'];
                    reKey = data['data']['rekey'];
                    dataList = data['data']['list'];
                    textModeHtml(data);
                    //年份图标每次检索都刷新
                    yearData = data['data']['yearResults'];
                    yearChart(0);
                } else {
                    textModeHtml(data);
                }
            } else {
                textModeHtml(data);
            }
        }
    })
}