<template>
<div>
    <div class="timebox">
    <span v-for="(time, index) in times" :key="index" @click="timechocie">
        {{time}}
    </span>
    <hr>
    <h3> 선택 시간 : {{timechoiced}} </h3>
    </div>
</div>
</template>

<script>

export default {
    name:'timeList',
    data(){
        return{
            timechoiced:"",
        }
    },
    props:{
        times: Array,
    },
    methods:{
        timechocie(){
            console.log(this.times[0])
        }
    }
    
}
</script>

<style>
.timebox{
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    font-family: 'notosans';
    text-align: center;
    

}
</style>