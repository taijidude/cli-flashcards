## question:
Example Type Alias 
<!-- Sides -->
## answer: 
```typescript
//Das in den Klammern ist eine type Definition
type User = {
	id: string
	avatar: string 
	name: string 
}
```
<!-- Card -->
## question: 
Interface Definition Typescript 
<!-- Sides -->
## answer: 
```typescript
interface User  {
	id: string;
	avatar: string; 
	name: string; 
}
```
<!-- Card -->
## question: 
Angular: Output List Content 
<!-- Sides -->
## answer: 
```html
@for (user of users ❗ Property ❗; track user.id) {
	<li>
		<app-user [user]="user" (select)="onSelected($event)" />
	</li>
}
```
<!-- Card -->
## question: 
Angular: Output Conditional Content
<!-- Sides -->
## answer: 
```html
<main>
	@if (selectedUser) {
		<app-task [name]="selectedUser.name : ''" />
	} @else {
		<p id="fallback"> Select a user to see their tasks! </p>
	}
</main>
```
<!-- Card -->
## question: 
Angular: String Interpolation
<!-- Sides -->
## answer: 
```html
<span> {{ selectedUser.name }} </span>
```
❗ - private properties are not reachable for the template
<!-- Card -->
## question: 
Angular: Getter functions
<!-- Sides -->
## answer: 
Could be used like a property
```typescript
export class UserComponent {
	selectedUser = DUMMY_USERS[randomIndex];
	get imagePath() {
		return 'assets/users/'+this.selectedUser.avatar;
	}
}
```
The Template: 
```html 
<div>
	<button>
		<img
			[src]="imagePath"
			[alt]="selectedUser.name"
		/>
	</button>
</div>


