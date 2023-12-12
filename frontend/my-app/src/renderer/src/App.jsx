import Versions from './components/Versions'
import icons from './assets/icons.svg'
import userService from './utils'


function App() {
  return (
    <div>
      <button onClick={() => userService.getdata()}>GetData</button>
      <h1>123</h1>
    </div>
  )

}

export default App
