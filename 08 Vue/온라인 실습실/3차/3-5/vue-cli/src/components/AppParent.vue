<template>
  <div class="border2">
    <hr>
    <h1> AppParent </h1>
    <input type="text" v-model="parentData" @input="fromParent"/>
    <p> appData: {{appData}} </p>
    <p> childData: {{childData}} </p>
    <AppChild
    :app-data="appData"
    :parent-data="parentData"
    @from-child="fromChild"/>
  </div>
</template>

<script>
import AppChild from '@/components/AppChild.vue';

export default {
    components: { AppChild },
    name:'AppParent',
    conponents:{
        AppChild,
    },
    props:{
        appData: String
    },
    data(){
        return{
            parentData:"",
            childData:"",
        }
    },
    methods:{
        fromParent(){
            this.$emit('from-parent', this.parentData);
        },
        fromChild(cd){
            this.childData = cd;
            this.$emit('from-child', this.childData)
        }
    }

}
</script>

<style>
.border2 {
    border : solid 1px red;
}
</style>