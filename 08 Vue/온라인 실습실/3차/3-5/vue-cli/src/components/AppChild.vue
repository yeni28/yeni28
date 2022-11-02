<template>
  <div class="border3">
    <hr>
    <h1> AppChild </h1>
    <input type="text" v-model="childData" @input="fromChild"/>
    <p> appData: {{appData}} </p>
    <p> parentData: {{parentData}} </p>
  </div>
</template>

<script>
export default {
    name:'AppChild',
    props:{
        parentData : String,
        appData : String
    },
    data(){
        return{
            childData:"",
        }
    },
    methods:{
        fromChild(){
            this.$emit('from-child', this.childData);
        }
    }
}
</script>

<style>
    .border3 {
    border : solid 1px blue;
}
</style>