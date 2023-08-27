<template>
    <v-card style="max-width: 700px; margin-top: 30px; padding: 30px; left: 50px;">
        <v-card-title>记录查询</v-card-title>
        <v-text-field
            lable="时间"
            v-model="time"
        ></v-text-field>
        <v-btn
            @click="fetch()"
        >查询</v-btn>
    </v-card>
    <v-card style="max-width: 700px; margin-top: 30px; padding: 30px; left: 50px;">
        <v-card-title>账单</v-card-title>
        <v-table>
            <thead>
                <tr>
                    <th>代付款人</th>
                    <th>金额</th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="(val, index) in data" :key="index">
                    <td>{{ val.payer }}</td>
                    <td>{{ val.money }}</td>
                </tr>
            </tbody>
        </v-table>
        <p>qj: {{ pay.qj }}</p>
        <p>zcy: {{ pay.zcy }}</p>
        <p>hmq: {{ pay.hmq }}</p>
        <p>lcy: {{ pay.lcy }}</p>
    </v-card>
</template>
  
<script lang="ts" setup>
import axios from '@/plugins/axios';
import { reactive, ref } from 'vue';

let time = ref("")
let data = reactive([] as any[])
function fetch() {
    axios.get('/query/' + time.value).then(
        (resp) => {
            for (let i of resp.data.data) {
                data.push(i)
            }
            calculate()
        }
    )
}

let pay = reactive({
    qj: 0,
    zcy: 0,
    hmq: 0,
    lcy: 0
})

function calculate() {
    console.log(data)
    for (let i of data) {
        pay.qj -= i.money / 4.0
        pay.zcy -= i.money / 4.0
        pay.hmq -= i.money / 4.0
        pay.lcy -= i.money / 4.0
        if (i.payer == 'qj')
            pay.qj += i.money
        else if (i.payer == 'zcy')
            pay.zcy += i.money
        else if (i.payer == 'hmq')
            pay.hmq += i.money
        else
            pay.lcy += i.money
    }
}

</script>