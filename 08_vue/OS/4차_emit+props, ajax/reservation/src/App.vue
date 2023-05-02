<template>
  <div id="app">
    <h1>버튼 박스 제작</h1>
    <h2>예약 페이지</h2>
    <h3>시간 선택</h3>
    <button @click="toggleTime(time)"
    v-for="time in times" v-bind:key="time"
    :class="{ active: selectedTimes.includes(time) }">
    {{time}}
    </button>
    <hr>
    <p><b>선택 시간: {{selectedTimes.join(" ")}}</b></p>
  </div>
</template>

<script>
export default {
  name:'app',
  data(){
    return{
      times: [
        "09:00","09:30","10:00","10:30","11:00","11:30","12:00","12:30","13:00","13:30",
        "14:00","14:30","15:00","15:30","16:00","16:30","17:00","17:30","18:00","18:30",
        "19:00","19:30","20:00","20:30","21:00","21:30","22:00","22:30","23:00","23:30",
      ],
      count :0,
      selectedTimes:[],
    }
  },  methods: {
    toggleTime(time) {
      const index = this.selectedTimes.indexOf(time);
      if (index > -1) {
        this.selectedTimes.splice(index, 1);
      } else if (this.selectedTimes.length < 5) {
        this.selectedTimes.push(time);
      } else {
        alert('5타임까지만 신청할 수 있습니다.');
      }
    },
  },
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
button {
  color:  #84898C;
  background-color: white;
  border: none;
  border-radius: 5px;
  padding: 5px 10px;
  margin: 5px;
  cursor: pointer;
}
button:hover:not(.active) {
  background-color: #658dc63d;
  color: #0F4C81;
}
button.active {
  background-color: #658dc63d;
  color: #0F4C81;
}
hr {
  color: #0F4C81;
}

</style>
