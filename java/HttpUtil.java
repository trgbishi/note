package util;


import org.apache.http.HttpEntity;
import org.apache.http.HttpResponse;
import org.apache.http.NameValuePair;
import org.apache.http.client.entity.UrlEncodedFormEntity;
import org.apache.http.client.methods.HttpDelete;
import org.apache.http.client.methods.HttpEntityEnclosingRequestBase;
import org.apache.http.client.methods.HttpGet;
import org.apache.http.client.methods.HttpPost;
import org.apache.http.entity.StringEntity;
import org.apache.http.impl.client.CloseableHttpClient;
import org.apache.http.impl.client.HttpClients;
import org.apache.http.util.EntityUtils;

import java.io.IOException;
import java.util.List;

/***
 * @Author zero
 * @Description Http工具类
 * @InitDate 15:24 2019/9/23
 * @Version 1.0
 **/
public class HttpUtil {
    public final static int SUCCESS_STATUS = 200;
    public final static int REFUSE_STATUS = 403;

    public final static int SUCCESS204 = 204;


    /***
     * @Author zero
     * @Description http get请求
     * @InitDate 9:58 2019/9/24
     * @Param [restApi]
     **/
    public static String httpClientGet(String restApi) {
        CloseableHttpClient client = HttpClients.createDefault();
        HttpGet httpget = new HttpGet(restApi);

        HttpResponse response;
        String result = null;
        try {
            response = client.execute(httpget);
            int statusCode = response.getStatusLine().getStatusCode();
            System.out.println(statusCode);
            if (statusCode == SUCCESS_STATUS) {
                HttpEntity httpEntity = response.getEntity();
                result = EntityUtils.toString(httpEntity, "utf-8");
            }

        } catch (IOException e) {
            e.printStackTrace();
        }finally {
            try {
                client.close();
            } catch (IOException e) {
                e.printStackTrace();
            }
        }

        return result;

    }

    /***
     * @Author zero
     * @Description http delete请求，返回status code
     * @InitDate 16:33 2019/9/24
     * @Param [restApi]
     **/
    public static Integer httpClientDelete(String restApi) {
        CloseableHttpClient client = HttpClients.createDefault();
        HttpDelete httpdel = new HttpDelete(restApi);

        HttpResponse response;
        try {
            response = client.execute(httpdel);
            return response.getStatusLine().getStatusCode();

        } catch (IOException e) {
            e.printStackTrace();
            return null;
        }finally {
            try {
                client.close();
            } catch (IOException e) {
                e.printStackTrace();
            }
        }


    }


    /***
     * @Author zero
     * @Description http post 传入 k-v参数
     * @InitDate 19:05 2019/9/23
     * @Param [restApi, parameters]
     **/
    public static String httpclientPost(String restApi, List<NameValuePair> parameters) {
        CloseableHttpClient client = HttpClients.createDefault();
        HttpPost post = new HttpPost(restApi);
        HttpResponse response;
        String result;
        try {
            post.setEntity(new UrlEncodedFormEntity(parameters, "utf-8"));
            response = client.execute(post);
            HttpEntity httpEntity = response.getEntity();
            result = EntityUtils.toString(httpEntity, "utf-8");
        } catch (IOException e) {
            e.printStackTrace();
            return null;
        }finally {
            try {
                client.close();
            } catch (IOException e) {
                e.printStackTrace();
            }
        }

        int statusCode = response.getStatusLine().getStatusCode();
        if (statusCode == SUCCESS_STATUS) {
            return result;
        } else {
            return null;
        }

    }

    /***
     * @Author zero
     * @Description 发送json串的http请求，httpRequest是具体的请求类型
     * @InitDate 10:36 2019/9/25
     * @Param [httpRequest, json]
     **/
    public static Integer httpRequestWithJSON(HttpEntityEnclosingRequestBase httpRequest, String json) {
        CloseableHttpClient httpclient = HttpClients.createDefault();
        try {
            httpRequest.addHeader("Content-type", "application/json; charset=utf-8");
            System.out.println("executing request " + httpRequest.getURI());

            StringEntity se = new StringEntity(json, "UTF-8");
            httpRequest.setEntity(se);
            System.out.println("request parameters " + json);

            HttpResponse response = httpclient.execute(httpRequest);
            int statusCode = response.getStatusLine().getStatusCode();
            System.out.println(statusCode);
            return statusCode;
        } catch (Exception e) {
            System.out.println("executing httpPostWithJSON error: " + e.getMessage());
        } finally {
            try {
                httpclient.close();
            } catch (IOException e) {
                System.out.println("executing httpPostWithJSON error: " + e.getMessage());
            }
        }

        return null;
    }




}