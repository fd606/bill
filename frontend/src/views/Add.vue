<template>
    <v-card style="max-width: 700px; margin-top: 30px; padding: 30px; left: 50px;">
        <v-card-title>新增记录</v-card-title>
        <v-form>
            <v-select
                label="代付款方"
                :items="['qj', 'zcy', 'hmq', 'lcy']"
                v-model="data.payer"
            ></v-select>
            <v-text-field
                label="金额"
                v-model="data.money"
            ></v-text-field>
            <v-btn @click="upload()">提交</v-btn>
        </v-form>
    </v-card>
</template>
  
<script lang="ts" setup>
import { reactive } from 'vue';
import axios from '@/plugins/axios'

let data = reactive({
    payer: '',
    money: 0
})

function upload(): void {
    console.log(data.payer)
    axios.post('/add', {
        payer: data.payer,
        money: data.money
    }).catch(console.log)
}

</script>
  