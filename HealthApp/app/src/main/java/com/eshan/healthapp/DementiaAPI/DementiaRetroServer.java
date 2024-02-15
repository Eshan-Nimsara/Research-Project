package com.eshan.healthapp.DementiaAPI;

import retrofit2.Retrofit;
import retrofit2.converter.gson.GsonConverterFactory;

public class DementiaRetroServer {

    private static final String BASE_URL = "https://ce35-175-157-15-72.ngrok.io";
    private static Retrofit retrofit;

    public static Retrofit connectRetrofit() {

        if (retrofit == null) {

            retrofit =  new Retrofit.Builder().baseUrl(BASE_URL)
                    .addConverterFactory(GsonConverterFactory.create())
                    .build();

        }

        return retrofit;

    }

}