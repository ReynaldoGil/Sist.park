fun enviarEstado(color: String) {
    val json = JSONObject()
    json.put("lugar", "A1") // ← Aquí defines cuál espacio representa ese sensor
    json.put("color", color)

    val body = RequestBody.create(
        MediaType.parse("application/json; charset=utf-8"),
        json.toString()
    )

    val request = Request.Builder()
        .url("http://192.168.9.66:5000/estado") // IP de tu laptop
        .post(body)
        .build()

    val client = OkHttpClient()
    client.newCall(request).enqueue(object : Callback {
        override fun onFailure(call: Call, e: IOException) {
            Log.e("HTTP", "Error: ${e.message}")
        }

        override fun onResponse(call: Call, response: Response) {
            Log.d("HTTP", "Estado enviado")
        }
    })
}
