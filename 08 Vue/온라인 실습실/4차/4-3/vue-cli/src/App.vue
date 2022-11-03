<template>
  <div id="app">
    <h1> SSAFY 상담 예약 시스템 </h1>
    <section class="section">
      <TimeTable @time-select="selectTime" @select-eric="selectEric" @select-tony="selectTony" class='timetable'/>
      <MyList 
      :select-time="selectedTimes"
      :selected-teacher="selectedTeacher" 
      class='list'
      />

    </section>
  </div>
</template>

<script>
import MyList from '@/components/MyList.vue'
import TimeTable from '@/components/TimeTable.vue';

export default {
  name: 'App',
  components: {
    MyList,
    TimeTable,
  },
  data(){
    return{
      selectedTeacher:"",
      selectedTimes:[]
    }
  },
  methods:{
    selectEric(inputData){
      this.selectedTeacher = inputData
    },
    selectTony(inputData){
      this.selectedTeacher = inputData },
    selectTime(inputData){
      // console.log(inputData)
      this.selectedTimes = inputData
      // console.log(this.selectedTimes)
      // this.selectedTimes.push(inputData)
    }
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
  font-family: 'noto';
}
.section{
  display:flex;
  width: 900px;
  box-shadow: 10px 10px 20px gray;
  margin: auto;
}
.list{
  width: 450px;
  height: 450px;
  background-color: rgb(209, 225, 255);
}
.timetable{
  width: 450px;
  height: 450px;

  
}


@font-face{
  font-family: 'noto';
  src:url(./assets/fonts/NotoSansKR-Regular.otf)
}

</style>
