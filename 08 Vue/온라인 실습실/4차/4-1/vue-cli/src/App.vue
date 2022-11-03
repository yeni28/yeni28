<template>
  <div id="app">
    <header>
    <h1>버튼 박스 제작</h1>
    </header>
    <section class="buttonbox">
      <h2> 예약 페이지 </h2>
      <h3> 시간 선택</h3>
      <div>
        <div class='timetable' >
        <span class='time' v-for="(time, index) in times" :key="index" @click="selectTime(time)" :class="{'selectedbtn':isSelected(time)}">
        {{time}}
        </span>
        </div>
        <hr style="width: 80%;">
        <h3>선택시간 : <span v-for="time in selectedTimes" :key="time"> {{time}} </span> </h3>
      </div>
    </section>
  </div>
</template>

<script>

export default {
  name: 'App',
  data(){
    return {
      selectedTimes:[],
      times:[
  "09:00","09:30","10:00","10:30","11:00","11:30","12:00","12:30","13:00","13:30",
  "14:00","14:30","15:00","15:30","16:00","16:30","17:00","17:30","18:00","18:30",
  "19:00","19:30","20:00","20:30","21:00","21:30","22:00","22:30","23:00","23:30",
    ],  
    }
  },
  
  methods:{
    selectTime(time){
        if (this.selectedTimes.includes(time)){
          const time_idx=this.selectedTimes.indexOf(time);
          this.selectedTimes.splice(time_idx,1);
          return;
        }

        // console.log(time)
        if (this.selectedTimes.length>=5){
          alert("5타임 까지만 신청할 수 있습니다.");
          return;
        }
        this.selectedTimes.push(time);
    },
    
    isSelected(time) {
      if(this.selectedTimes.includes(time)){
        return true;
      } else {
        return false;
      }
      }
  },

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
  font-family: 'notosans';
}
.buttonbox{
  box-shadow: 0px 0px 20px lightgray;
  padding : 5px;
  left: 50%;
  right: 50%;
  margin-left: auto;
  margin-right: auto;
  width: 500px;
  height: 400px;

}

.timetable{
  display: flex;
  flex-wrap: wrap;
  padding: 5px;
  justify-content: center;

}

.time{
  margin: 5px;
  color:#a6a9ad
  
}

.selectedbtn{
  background-color: #c6e4ff;
  color: #2c649c;
  
}
@font-face{
  font-family:'notosans';
  src: url('../public/fonts/NotoSansKR-Regular.otf')
}
</style>
